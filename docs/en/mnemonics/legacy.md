---
title: Legacy Mnemonic Scheme
---

The legacy mnemonic scheme is the oldest and most widely-used mnemonic scheme in the Monero ecosystem. It comprises a total of 25 words, where the first 24 words are for the seed and the last word is for the checksum. The checksum word is used to verify the correctness of the seed.

The first 24 words are randomly selected from a list of 1626 words described in [`src/mnemonics/english.h`](https://github.com/monero-project/monero/blob/master/src/mnemonics/english.h) (Wordlists available for other languages can be found in [`src/mnemonics`](https://github.com/monero-project/monero/tree/master/src/mnemonics)). The checksum word is selected by calculating the [CRC32 checksum index](https://en.wikipedia.org/wiki/Cyclic_redundancy_check) of a string that is made by concatenating the first `prefix_length`ed characters of each selected word. The `prefix_length` is the number of characters to be used from each word to calculate the checksum. [In the case of English wordlist, the `prefix_length` is 3](https://github.com/monero-project/monero/blob/master/src/mnemonics/english.h#L52C47-L52C48).

Example of calculating the checksum word:

1. Randomly select (don't forget that randomness should be [cryptographically secure](https://en.wikipedia.org/wiki/Cryptographically_secure_pseudorandom_number_generator)) 24 words from the wordlist. For example, let's say the chosen words are `lush bagpipe stacking mice imitate village gang efficient strained different together vain puck roped pancakes shocking liar moisture memoir sorry syndrome kettle swept dehydrate`.
2. Take the first 3 characters of each word and concatenate them. In this case, it will be `lusbagstamicimivilganeffstrdiftogvaipucroppansholiamoimemsorsynketswedeh`.
3. Calculate the CRC32 checksum of the concatenated string. In this case, the checksum gives us the decimal number `2248614488`.
4. Take the checksum index modulo 24. In this case, the modulo gives us `8`.
5. The 8th index of the wordlist is `strained` (don't forget that the wordlist is 0-indexed). So, the checksum word is `strained`.

### Wordlists

Wordlists used in the legacy mnemonic scheme are unique to Monero and were contributed by the Monero community; one exception is the 'EnglishOld' wordlist, which was originally sourced from the Electrum Bitcoin wallet ([see here](https://monero.stackexchange.com/questions/3559/electrum-seed-word-list-for-monero-official-electrum-wordlist-english-why)), and is no longer used by either project.

Supported languages include German, English, Spanish, French, Italian, Dutch, Portuguese, Russian, Japanese, Chinese (simplified), Esperanto, and Lojban.

### Encrypted seeds

The legacy mnemonic scheme supports encrypted seeds, also called seed offsets or seed passphrases. This is different from wallet files, which are symmetrically encrypted on-disk.

Seed encryption works by applying the [CryptoNight hashing function](../proof-of-work/cryptonight.md) to the provided passphrase and adding the result to the wallet's keys. When restoring an encrypted wallet, the hash can again be calculated and subtracted upon being provided by the user.
