---
title: Legacy Mnemonic Scheme
---

The legacy mnemonic scheme is the oldest and most widely-used mnemonic scheme in the Monero ecosystem. It comprises a total of 25 words, where the first 24 words encode the private spend key and the last word is for the checksum. The checksum word is used to verify the correctness of the seed.

The words are taken from a list of 1626 words described in [`src/mnemonics/english.h`](https://github.com/monero-project/monero/blob/master/src/mnemonics/english.h) (Wordlists available for other languages can be found in [`src/mnemonics`](https://github.com/monero-project/monero/tree/master/src/mnemonics)). See [Encoding](#encoding) for how the words are derived from the key.

The checksum word is selected by calculating the [CRC32 checksum index](https://en.wikipedia.org/wiki/Cyclic_redundancy_check) of a string that is made by concatenating the first `prefix_length`ed characters of each selected word. The `prefix_length` is the number of characters to be used from each word to calculate the checksum. [In the case of English wordlist, the `prefix_length` is 3](https://github.com/monero-project/monero/blob/master/src/mnemonics/english.h#L52C47-L52C48).

Example of calculating the checksum word:

1. Take the 24 seed words. For example, `lush bagpipe stacking mice imitate village gang efficient strained different together vain puck roped pancakes shocking liar moisture memoir sorry syndrome kettle swept dehydrate`.
2. Take the first 3 characters of each word and concatenate them. In this case, it will be `lusbagstamicimivilganeffstrdiftogvaipucroppansholiamoimemsorsynketswedeh`.
3. Calculate the CRC32 checksum of the concatenated string. In this case, the checksum gives us the decimal number `2248614488`.
4. Take the checksum modulo 24. In this case, the modulo gives us `8`.
5. The checksum is the word at the 8th index. The index is 0-based, so the checksum is the 9th of the 24 seed words. In this example, the checksum word is `strained`.

### Encoding

The 32-byte private spend key is split into eight 4-byte chunks, each read as a little-endian 32-bit integer `x`. Each chunk becomes three words, where `n` is the wordlist size (1626) and `w1`-`w3` are word indices (`/` is integer division):

```
w1 = x % n
w2 = (x / n + w1) % n
w3 = (x / n / n + w2) % n
```

Three words are enough since 1626^3 > 2^32. Decoding reverses this with `x = w1 + n*((w2 - w1) mod n) + n^2*((w3 - w2) mod n)`; word combinations that don't fit in 32 bits are rejected as invalid.

The private view key isn't stored in the mnemonic; it is the [Keccak-256](../cryptography/keccak-256.md) hash of the private spend key, reduced modulo `l` (the order of the ed25519 base point).

### Wordlists

Wordlists used in the legacy mnemonic scheme are unique to Monero and were contributed by the Monero community; one exception is the 'EnglishOld' wordlist, which was originally sourced from the Electrum Bitcoin wallet ([see here](https://monero.stackexchange.com/questions/3559/electrum-seed-word-list-for-monero-official-electrum-wordlist-english-why)), and is no longer used by either project.

Supported languages include German, English, Spanish, French, Italian, Dutch, Portuguese, Russian, Japanese, Chinese (simplified), Esperanto, and Lojban.

### Encrypted seeds

The legacy mnemonic scheme supports encrypted seeds, also called seed offsets or seed passphrases. This is different from wallet files, which are symmetrically encrypted on-disk.

Seed encryption works by applying the [CryptoNight hashing function](../proof-of-work/cryptonight.md) to the provided passphrase and adding the result to the wallet's keys. When restoring an encrypted wallet, the hash can again be calculated and subtracted upon being provided by the user.
