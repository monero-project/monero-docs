---
title: MyMonero Mnemonic Scheme
---

The MyMonero scheme can be thought of as the 13-word version of the [Legacy Mnemonic Scheme](./legacy.md). Most processes remain the same in both schemes, but of course there are things that are different. For example, the method for deriving the checksum and the method for deriving the hexadecimal seed are the same, but since MyMonero generates a shorter hexadecimal seed, deriving private keys from that hexadecimal seed is different than in Legacy. 

For users looking to convert a MyMonero seed into a legacy one, an offline converter can be found at [xmr.llcoins.net](https://github.com/luigi1111/xmr.llcoins.net/).
 
The MyMonero scheme was initially used by MyMonero web and mobile wallet, but other projects also adopted this scheme. The scheme is designed to be more user-friendly and easier to remember than the legacy scheme.

The MyMonero scheme comprises a total of 13 words, where the first 12 words are for the seed and the last word is for the checksum. The checksum word is used to verify the correctness of the seed.

Deriving checksum process is the same as the [Legacy Mnemonic Scheme](./legacy.md), you can check out the details from that page.
