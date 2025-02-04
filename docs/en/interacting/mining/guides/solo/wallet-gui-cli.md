---
title: How to mine with Monero GUI amd CLI wallets
---

## Requirements

- [Monero GUI wallet](https://getmonero.org/downloads)
- Minimum {{ lmdb_size_pruned }} GiB free space
- A fully synced node, managed by Monero GUI

## Notes

- [GUI] The miner used for the P2Pool integration is more optimized than the one used for solo mining.
- Mining using XMRig may also produce even better hashrates than Monero GUI.
- [Solo] The purpose of GUI or CLI wallet is to control the miner. The actual mining process is done by the node (monerod).

If the highest hashrates possible are important to you, check out the [solo XMRig guide](./xmrig-solo.md), [XMRig + P2Pool CLI guide](../p2pool/xmrig-p2pool.md), or the [gupax.io XMRig + P2Pool GUI](https://gupax.io).

## Get Started

=== "Monero GUI"

    1. Click on the Advanced tab, then Mining
    2. Select whether to mine Solo or to use P2Pool
    3. Select the number of threads to use
    4. Click the "Start mining" button

=== "Monero CLI"

    _NOTE_: Monero CLI cannot use P2Pool.

    1. Connect Monero CLI to a node's Unrestricted RPC port
    2. Enter the command `start_mining <NUM_OF_THREADS>`

=== "Monerod"

    You can also control mining manually via monerod

    1. Launch and sync monerod
    2. Enter the command `start_mining <PRIMARY_WALLET_ADDRESS> <NUM_OF_THREADS>`
