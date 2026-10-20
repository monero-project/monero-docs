---
title: Hard Forks
---

# Hard Forks

Monero uses scheduled network upgrades (hard forks) in order to introduce changes to consensus rules. Each upgrade activates at a fixed block height, and nodes that have not upgraded to a compatible release will reject the new blocks and "fall off" of the network.

!!! info ""
    Users and service providers should run current releases and upgrade before a scheduled network upgrade. The required software is published in advance of the activation height.

    Here, the "minimum" version is the first release that follows the new consensus rules. The "recommended" version may include bug fixes and other features that do not affect consensus logic.

Upgrades usually come in pairs, with the first fork introducing a new format and allowing both old and new, and the second fork, roughly a day (720 blocks) later, forbidding the old format. This gives transactions which are already in the mempool time to be mined.

## Mainnet

Dates are in the format of YYYY-MM-DD. Version 1 covers blocks 1 to 1009826.

| Height  | Date       | Version | Minimum   | Recommended | Summary                                                                        |
| ------- | ---------- | ------- | --------- | ----------- | ------------------------------------------------------------------------------ |
| 1009827 | 2016-03-22 | v2      | v0.9.4    | v0.9.4      | Ring size >= 3, 120 second block time, 60 kB penalty-free block size           |
| 1141317 | 2016-09-21 | v3      | v0.9.4    | v0.10.0     | Coinbase split into denominations                                              |
| 1220516 | 2017-01-05 | v4      | v0.10.1   | v0.10.2.1   | RingCT transactions allowed, dynamic fees                                      |
| 1288616 | 2017-04-15 | v5      | v0.10.3.0 | v0.10.3.1   | 300 kB penalty-free block size, adjusted fee algorithm                         |
| 1400000 | 2017-09-16 | v6      | v0.11.0.0 | v0.11.0.0   | RingCT required, ring size >= 5                                                |
| 1546000 | 2018-04-06 | v7      | v0.12.0.0 | v0.12.3.0   | CryptoNight variant 1, ring size >= 7, sorted inputs                           |
| 1685555 | 2018-10-18 | v8      | v0.13.0.0 | v0.13.0.4   | CryptoNight variant 2, Bulletproofs allowed, fixed ring size 11, per-byte fees |
| 1686275 | 2018-10-19 | v9      | v0.13.0.0 | v0.13.0.4   | Bulletproofs required                                                          |
| 1788000 | 2019-03-09 | v10     | v0.14.0.0 | v0.14.1.2   | CryptoNight-R, long-term block weight, more compact Bulletproofs format        |
| 1788720 | 2019-03-10 | v11     | v0.14.0.0 | v0.14.1.2   | Old Bulletproofs format forbidden                                              |
| 1978433 | 2019-11-30 | v12     | v0.15.0.0 | v0.16.0.0   | RandomX, >= 2 outputs, uniform ring size, 10 block spendable age               |
| 2210000 | 2020-10-17 | v13     | v0.17.0.0 | v0.17.3.2   | CLSAG allowed, exact coinbase amount                                           |
| 2210720 | 2020-10-18 | v14     | v0.17.1.1 | v0.17.3.2   | MLSAG forbidden                                                                |
| 2688888 | 2022-08-13 | v15     | v0.18.0.0 | v0.18.5.4   | Ring size 16, Bulletproofs+, view tags, 2021 scaling                           |
| 2689608 | 2022-08-14 | v16     | v0.18.0.0 | v0.18.5.4   | Old transaction formats forbidden, view tags required                          |

## Consensus changes

The changes below are the rules enforced by `monerod` for blocks at or above each fork's activation height. The constants in parentheses are defined in [`cryptonote_config.h`](https://github.com/monero-project/monero/blob/master/src/cryptonote_config.h).

### v1

- Original CryptoNote rules
- 60 second block time (`DIFFICULTY_TARGET_V1`)
- [CryptoNight](../proof-of-work/cryptonight.md) proof of work
- 20,000 byte penalty-free block size (`CRYPTONOTE_BLOCK_GRANTED_FULL_REWARD_ZONE_V1`)

### v2

- 120 second block time (`DIFFICULTY_TARGET_V2`)
- Minimum ring size of 3, unless spending outputs that do not have enough decoys on the chain
- Outputs of non-RingCT transactions must be valid decomposed amounts (no dust)
- 60,000 byte penalty-free block size (`CRYPTONOTE_BLOCK_GRANTED_FULL_REWARD_ZONE_V2`)
- Miners may claim less than the full block reward (allowed until v13). The unclaimed amount is pushed back into future emission

### v3

- Coinbase outputs must be valid decomposed amounts
- Outputs of version 2 (RingCT) transactions must have a zero cleartext amount

### v4

- Version 2 (RingCT) transactions are allowed
- Dynamic fees (`HF_VERSION_DYNAMIC_FEE`)

### v5

- 300,000 byte penalty-free block size (`CRYPTONOTE_BLOCK_GRANTED_FULL_REWARD_ZONE_V5`)
- Adjusted dynamic fee algorithm

### v6

- RingCT is required (`HF_VERSION_ENFORCE_RCT`). Version 1 transactions are only accepted when spending pre-RingCT outputs that do not have enough decoys
- Minimum ring size of 5 (`HF_VERSION_MIN_MIXIN_4`)

### v7

- CryptoNight variant 1 (`HF_VERSION_CRYPTONIGHT_VARIANT_1`)
- Minimum ring size of 7 (`HF_VERSION_MIN_MIXIN_6`)
- Transaction inputs must be sorted by key image

### v8

- CryptoNight variant 2
- Bulletproofs range proofs are allowed
- Ring size fixed at exactly 11 (`HF_VERSION_MIN_MIXIN_10`)
- Per-byte fees (`HF_VERSION_PER_BYTE_FEE`)
- Maximum transaction size of half the penalty-free block size

### v9

- Borromean range proofs are forbidden. Bulletproofs are required

### v10

- CryptoNight-R (CryptoNight variant 4)
- `RCTTypeBulletproof2`, a more compact RingCT format, is allowed (`HF_VERSION_SMALLER_BP`)
- Long-term block weight algorithm (`HF_VERSION_LONG_TERM_BLOCK_WEIGHT`)

### v11

- `RCTTypeBulletproof` is forbidden. Only `RCTTypeBulletproof2` is accepted

### v12

- [RandomX](../proof-of-work/random-x.md) proof of work (`RX_BLOCK_VERSION`)
- RingCT transactions must have at least 2 outputs (`HF_VERSION_MIN_2_OUTPUTS`)
- Coinbase transactions must be version 2 (`HF_VERSION_MIN_V2_COINBASE_TX`)
- RingCT signatures in coinbase transactions are forbidden (`HF_VERSION_REJECT_SIGS_IN_COINBASE`)
- All inputs in a transaction must use the same ring size (`HF_VERSION_SAME_MIXIN`)
- Outputs cannot be spent until they are 10 blocks old (`HF_VERSION_ENFORCE_MIN_AGE`, `CRYPTONOTE_DEFAULT_TX_SPENDABLE_AGE`)
- The block reward penalty uses the effective short-term median block weight (`HF_VERSION_EFFECTIVE_SHORT_TERM_MEDIAN_IN_PENALTY`)

### v13

- CLSAG ring signatures (`RCTTypeCLSAG`) are allowed (`HF_VERSION_CLSAG`)
- Coinbase transactions must claim exactly the block reward plus fees (`HF_VERSION_EXACT_COINBASE`)
- Time-based unlock times are checked against the blockchain's adjusted time instead of the node's local clock (`HF_VERSION_DETERMINISTIC_UNLOCK_TIME`)

### v14

- MLSAG ring signatures are forbidden. Only CLSAG is accepted
    - Two MLSAG transactions that were in the mempool at the time of the fork are grandfathered in

### v15

- Ring size of 16 (`HF_VERSION_MIN_MIXIN_15`). Ring size 11 is still accepted during this fork as a grace period
- Bulletproofs+ range proofs (`RCTTypeBulletproofPlus`) are allowed (`HF_VERSION_BULLETPROOF_PLUS`)
- View tags (`txout_to_tagged_key`) are allowed (`HF_VERSION_VIEW_TAGS`). All outputs in a transaction must use the same output type
- Adjusted dynamic block weight and fee algorithm (`HF_VERSION_2021_SCALING`)

### v16

- Ring size fixed at exactly 16
- Bulletproofs (`RCTTypeBulletproof`, `RCTTypeBulletproof2`, `RCTTypeCLSAG`) are forbidden. Only Bulletproofs+ is accepted
- All outputs must have view tags

## Stagenet and Testnet

[Stagenet and testnet](../infrastructure/networks.md) follow the same consensus rules as mainnet for each version, but activate them at different heights.

| Version | Stagenet height | Testnet height |
| ------- | --------------- | -------------- |
| v1      | 1               | 1              |
| v2      | 32000           | 624634         |
| v3      | 33000           | 800500         |
| v4      | 34000           | 801219         |
| v5      | 35000           | 802660         |
| v6      | 36000           | 971400         |
| v7      | 37000           | 1057027        |
| v8      | 176456          | 1057058        |
| v9      | 177176          | 1057778        |
| v10     | 269000          | 1154318        |
| v11     | 269720          | 1155038        |
| v12     | 454721          | 1308737        |
| v13     | 675405          | 1543939        |
| v14     | 676125          | 1544659        |
| v15     | 1151000         | 1982800        |
| v16     | 1151720         | 1983520        |

## Sources

- [Fork heights](https://github.com/monero-project/monero/blob/master/src/hardforks/hardforks.cpp) (`src/hardforks/hardforks.cpp`)
- [Upgrade schedule](https://github.com/monero-project/monero/blob/master/README.md#scheduled-softwarenetwork-upgrades) (`README.md`)
- [Consensus checks](https://github.com/monero-project/monero/blob/master/src/cryptonote_core/blockchain.cpp) (`src/cryptonote_core/blockchain.cpp`)
