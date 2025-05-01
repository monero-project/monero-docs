---
title: Polyseed Mnemonic Scheme
---

> **Note**: Adapted for monero-docs. The expanded original README is available on Tevador's [Polyseed repository](https://github.com/tevador/polyseed)

The polyseed mnemonic scheme was initially intended for implementation alongside Seraphis and Jamtis, though it was adopted by the community ahead of schedule due to its efficiency, simplicity and security. One such UX improvement is the embedding of the [wallet birthday (restore height)](#wallet-birthday-restore-height), which removes the need for users to store the info manually.

Unlike the legacy mnemonic scheme, the polyseed mechanism does not allow you to choose the words from a wordlist. Instead, the words are generated from the [secret seed](#secret-seed), feature bits and birthday bits. The feature bits are used to determine the wallet features and the birthday bits are used to determine the [wallet birthday](#wallet-birthday-restore-height).

### Encoding

Each word contains 11 bits of information that is the index of the word from the polyseed, which is a list of 2048 words (Notice that 2^11 is 2048). The words are determined by the following formula:

| Word | Contents |
|----|----------|
|1   | Checksum (11 bits) |
|2-6 | Secret seed (10 bits) + Features (1 bit) |
|7-16| Secret seed (10 bits) + Birthday (1 bit) |

In total, there are 11 bits for the checksum, 150 bits for the secret seed, 5 feature bits and 10 birthday bits.

### Wallet birthday (Restore height)

The mnemonic phrase stores the approximate date when the wallet was created. This allows the seed to be generated offline without access to the blockchain. Wallet software can easily convert a date to the corresponding block height when restoring a seed.

The wallet birthday has a resolution of 2629746 seconds (1/12 of the average Gregorian year). All dates between November 2021 and February 2107 can be represented (Total of 1024 months, as we have 10 bits for it, 2^10 = 1024).

### Secret seed

Polyseed was designed for the 128-bit security level. This corresponds to the security of the ed25519 elliptic curve, which requires [about 2^126 operations](https://safecurves.cr.yp.to/rho.html) to break a key.

The private key is derived from the 150-bit secret seed using PBKDF2-HMAC-SHA256 with 10000 iterations. The KDF parameters were selected to allow for the key to be derived by hardware wallets.
