---
title: Wallet Files
---

# Wallet files

Monero wallets are typically stored in dedicated wallet files; each wallet is comprised of a keys file and a cache file. The former stores the wallet's keys and settings in JSON format, while the latter stores transaction data, contacts, address labels, block hashes, attributes, and other related information. Both files are encrypted using the wallet's password.

For example, a wallet named "foobar" would have two files: `foobar` and `foobar.keys`.

## Keys file

The keys file (`<walletname>.keys`) holds everything needed to restore access to the wallet (secret keys, seed language, and the wallet's settings). If the cache file is lost, the wallet can still be reopened from the keys file alone and will rescan the blockchain.

On disk, the keys file is a binary-serialized structure containing a random ChaCha20 IV (Initialization Vector, also called a nonce), as well as the encrypted contents. Once decrypted, the contents are a JSON object. Its `key_data` field holds the wallet's account, serialized in the `epee` binary format (see [here](https://github.com/monero-project/monero/blob/master/docs/PORTABLE_STORAGE.md)), and the remaining fields store wallet settings.

### Account data (`key_data`)

| Field                  | Description                                                                                                   |
| ---------------------- | ------------------------------------------------------------------------------------------------------------- |
| `m_account_address`    | The wallet's primary address (public spend and view keys).                                                    |
| `m_spend_secret_key`   | The secret spend key, empty for watch-only wallets.                                                           |
| `m_view_secret_key`    | The secret view key.                                                                                          |
| `m_multisig_keys`      | The wallet's multisig secret keys (multisig wallets only).                                                    |
| `m_encryption_iv`      | The IV used to additionally encrypt the secret keys (see below).                                              |
| `m_polyseed`           | The stored [Polyseed](#polyseed), for wallets created from a Polyseed mnemonic.                               |
| `m_passphrase`         | A passphrase written by wallets built on [`monero_c`](#monero_c-passphrase). Monero itself never writes this. |
| `m_creation_timestamp` | The wallet's creation time, used to skip scanning blocks that are older than the wallet.                      |

In addition to the encryption of the whole file, the secret values in `key_data` (the spend and view keys, multisig keys, Polyseed, and passphrase) are XORed with a ChaCha20 keystream derived from the password and `m_encryption_iv`. This is indicated by the `encrypted_secret_keys` field in the JSON.

### Settings

The other fields of the JSON object are mostly wallet settings, many of which can be changed using the `set` command in the CLI wallet. Notable fields include:

| Field                                                      | Description                                                                                          |
| ---------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `seed_language`                                            | The language of the mnemonic seed.                                                                   |
| `nettype`                                                  | The network the wallet belongs to (`0` for mainnet, `1` for testnet, `2` for stagenet).              |
| `watch_only`                                               | `1` if the wallet has no secret spend key.                                                           |
| `key_on_device`                                            | The key storage type, e.g. software or a hardware wallet such as Ledger or Trezor.                   |
| `device_name`, `device_derivation_path`                    | Hardware wallet settings.                                                                            |
| Multisig commands (`multisig`, `multisig_threshold`, etc.) | Multisig state.                                                                                      |
| `enable_multisig`                                          | Whether the (experimental) multisig feature is enabled.                                              |
| `polyseed`                                                 | `1` if the wallet was created using a Polyseed.                                                      |
| `refresh_height`, `skip_to_height`                         | The restore height, and the height the wallet scan can skip to.                                      |
| `ask_password`                                             | When the wallet prompts for the password.                                                            |
| `default_priority`, `default_mixin`                        | Default transaction fee priority and ring size.                                                      |
| `subaddress_lookahead_major`, `subaddress_lookahead_minor` | How many subaddresses ahead of the last used one are scanned for.                                    |
| `background_sync_type`, `custom_background_key`            | [Background sync](#background-sync-files) settings.                                                  |
| `original_address`, `original_view_secret_key`             | Kept for multisig wallets so that the wallet can still identify its original (pre-multisig) address. |

The keys file also contains fields that are no longer used and only remain for backwards compatibility, such as `persistent_rpc_client_id`, `auto_mine_for_rpc_payment`, and `credits_target` from the removed pay-for-RPC system.

### Polyseed

Wallets created from a [Polyseed](https://github.com/tevador/polyseed) mnemonic set `polyseed` to `1` in the JSON and store the encoded Polyseed in `m_polyseed` within `key_data`. Because the Polyseed itself is stored, the wallet can show the original 16-word mnemonic again. A Polyseed passphrase (seed offset) is not stored, so it must be backed up separately.

This layout is compatible with wallets built on `monero_c`, which supported Polyseed before Monero did. Feather Wallet stores its Polyseed differently (see [Feather Wallet attributes](#feather-wallet-attributes)).

When a Polyseed wallet becomes a multisig wallet, `polyseed` is set back to `0`, but the stored Polyseed itself is kept.

### `monero_c` passphrase

Wallet apps built on the [`monero_c`](https://github.com/MrCyjaneK/monero_c) library (e.g. Cake Wallet and Stack Wallet) store the Polyseed passphrase in the keys file under `m_passphrase` in `key_data`. Monero does not use this value itself; it only preserves it for compatibility reasons, encrypted like other secret values, when the keys file is read and rewritten. This means that these wallets will keep working after being opened by Monero.

Wallet developers should not rely on this field as long-term storage for the passphrase. Monero's source recommends moving it somewhere else in the wallet files early and ignoring the field afterwards.

The passphrase is removed when a watch-only copy of the wallet is exported (see [Watch-only exports](#watch-only-exports)).

## Cache file

The cache file (`<walletname>`, with no file extension) is a binary-serialized structure containing a random ChaCha20 IV and the encrypted wallet cache. It holds data that can mostly be recreated by rescanning the blockchain, including:

- Known block hashes and the wallet's outputs (transfers), key images, and incoming and outgoing payments
- Unconfirmed transactions and scanned pool transactions
- Subaddresses and their labels, and account tags
- Attributes (see below)

It also holds some data that **cannot** be recovered by rescanning:

- Transaction secret keys (`m_tx_keys`, `m_additional_tx_keys`), used to prove payments
- Transaction notes
- The address book
- Attributes

If you delete the cache file to force a full rescan, this data is lost. Back up the cache file along with the keys file if you want to keep it.

### Attributes

Attributes are arbitrary string key-value pairs stored in the wallet cache. Monero itself stores only one attribute, the wallet's description, under the key `wallet2.description`, which is set with the `set_description` command in the CLI wallet.

Any wallet app can store its own attributes in a wallet file, and many do. To prevent different apps from overwriting or misreading each other's values, Monero recommends naming keys `<client name>.<value name>`.

Attributes can be read and written with:

- the [`get_attribute`](https://docs.getmonero.org/rpc-library/wallet-rpc/#get_attribute) and [`set_attribute`](https://docs.getmonero.org/rpc-library/wallet-rpc/#set_attribute) methods of `monero-wallet-rpc`
- `getCacheAttribute` and `setCacheAttribute` in the wallet API (`wallet2_api.h`), which are also used by `monero_c`

Because attributes are stored in the cache file, they are lost if the cache file is deleted.

#### Feather Wallet attributes

Feather Wallet uses several attributes of its own. These are defined by Feather, not by Monero, and may change:

| Key                         | Description                                                     |
| --------------------------- | --------------------------------------------------------------- |
| `feather.seed`              | The wallet's Polyseed mnemonic.                                 |
| `feather.seedoffset`        | The Polyseed passphrase (seed offset).                          |
| `feather.pinnedaddresses`   | Comma-separated list of pinned subaddresses.                    |
| `feather.hiddenaddresses`   | Comma-separated list of hidden subaddresses.                    |
| `wallet.notes`              | Free-form wallet notes.                                         |
| `coin.description:<pubkey>` | A description attached to the output with the given public key. |

Feather stores its Polyseed in the `feather.seed` attribute rather than in the keys file. When the CLI wallet opens such a wallet file, it detects the Polyseed in this attribute and rewrites the keys file to use Monero's native [Polyseed](#polyseed) storage. The wallet stays compatible with Feather. The `feather.seedoffset` attribute is ignored, because Monero does not store passphrases.

## File encryption

The ChaCha20 stream cipher is used to encrypt the wallet files, along with the memory-hard [CryptoNight hash function](https://docs.getmonero.org/proof-of-work/cryptonight/), which is used as a [KDF](https://en.wikipedia.org/wiki/Key_derivation_function).

The original CryptoNight variant (variant 0) is used, and it is applied once by default. The number of rounds can be increased with the `--kdf-rounds` option, which must then be given every time the wallet is opened.

- **Keys file:** encrypted with the password-derived key. A new random IV is generated every time the file is written.
- **Cache file:** encrypted with a separate key, the Keccak hash of the password-derived key followed by a domain separator byte (`0x8D`). It also uses a new random IV on every write.

Very old wallets encrypted their files with ChaCha8, or derived the cache key from the wallet's secret keys instead of the password. Monero can still read these files, and upgrades them when it rewrites them.

## Other files

Depending on the wallet's configuration, a few other files may appear next to the keys and cache files.

### Address files

For non-mainnet wallets, an additional unencrypted file (in the format of `<walletname>.address.txt`) will be created containing the wallet's primary address.

The address file can also be created for mainnet wallets by passing `--create-address-file` to `monero-wallet-cli` when creating the wallet.

### Watch-only exports

The `save_watch_only` command in the CLI wallet writes a watch-only copy of the keys file to `<walletname>-watchonly.keys`, encrypted with a separate password. The secret spend key, multisig keys, Polyseed, `monero_c` passphrase, and background sync settings are left out of this copy.

### Background sync files

When background sync is enabled, the wallet creates a separate background wallet (`<walletname>.background` and `<walletname>.background.keys`). It contains only the view key, which allows the wallet to keep scanning while it is locked. With the custom password background sync type, these files are encrypted with keys derived from the background sync password instead of the wallet password.

### Multisig messaging system file

If the multisig messaging system (MMS) is active, its state is stored in `<walletname>.mms`.

### Temporary and recovery files

- `<walletname>.new` and `<walletname>.keys.new` are temporary files written while saving. They replace the existing files once the write has completed, so a crash during saving does not corrupt the wallet.
- `<walletname>.unportable` is a backup copy that is made when the wallet loads a cache written in an old, platform-specific format.

### Shared ring database

The shared ring database is not stored with the wallet. It lives in `~/.shared-ringdb` by default on POSIX systems (configurable with `--shared-ringdb-dir`) and is shared by all wallets on the system.

## References

- [Feather Wallet docs](https://docs.featherwallet.org/guides/wallet-files)
- Monero source ([`wallet2.cpp`](https://github.com/monero-project/monero/blob/master/src/wallet/wallet2.cpp) and [`account.h`](https://github.com/monero-project/monero/blob/master/src/cryptonote_basic/account.h))
