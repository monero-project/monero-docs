---
title: Wallet Files
---

# Wallet files

Monero wallets are typically stored in dedicated wallet files; each wallet is comprised of a keys file and a cache file. The former stores the wallet's keys and settings in JSON format, while the latter stores transaction data, contacts, address labels, block hashes, and other related information. Both files are encrypted using the wallet's password.

For example, a wallet named "foobar" would have two files: `foobar` and `foobar.keys`.

## File encryption

The ChaCha20 stream cipher is used to encrypt the wallet files, along with the memory-hard [CryptoNight hash function](https://docs.getmonero.org/proof-of-work/cryptonight/), which is used as a [KDF](https://en.wikipedia.org/wiki/Key_derivation_function).

## Address files

For non-mainnet wallets, an additional unencrypted file (in the format of `<walletname>.address.txt`) will be created containing the wallet's primary address.

## References

* [Feather Wallet docs](https://docs.featherwallet.org/guides/wallet-files)
