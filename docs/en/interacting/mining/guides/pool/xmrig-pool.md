---
title: How to mine on a Pool with XMRig
---

## Requirements
### Wallet

Before starting, you already need to have a wallet configured and
working. The pool needs to know your wallet address to be able to send
payments there.    
When mining on a pool, it's recommended to use an unused wallet, subaccount or subaddress.

### XMRig Software

The XMRig developer provides pre-built binaries for Ubuntu Linux LTS releases, MacOS 11+, and FreeBSD.

- You can download XMRig from: [XMRig.com](https://xmrig.com/download) or [GitHub](https://github.com/xmrig/xmrig/releases/latest).
- You can build XMRig from source. Take a look at [XMRig's docs](https://xmrig.com/docs/miner/build)

## Selecting a pool

There are numerous pools to choose from. You can find a list at [miningpoolstats.stream/monero](https://miningpoolstats.stream/monero).

Keep in mind that you should _not_ choose one of the top 3 pools. Choosing a smaller
pool helps keep the network decentralised.

Whatever pool you choose, be sure to pay attention to the pool's fees and the minimum
withdrawal. You won't be able to withdraw your funds until you reach the pool's
threshold. Each pool has their own minimums and fees.

## Configuring XMRig

The pool website will typically have instructions on how to setup and run XMRig.    
See the [official docs](https://xmrig.com/docs/miner/config) for instructions on setting up using a config file and further suggestions.

Start the miner using the parameters shown to you by the Pool's website.

If you see green messages saying that shares have been accepted,
congratulations, everything is working!

{% include 'mining_footer' %}

## Going Further

* Consider using a subaddress just for mining, to prevent your address
  being linked to different services.
* [Consider using Tor to connect to the
  pool](https://xmrig.com/docs/miner/tor) (or to a hidden service pool
  like HashVault and MoneroOcean). This hides mining
  activity from your ISP, and prevents the pool from knowing who you
  are.

Adapted from [monero-site](https://github.com/monero-project/monero-site/blob/ee03c625e6257f25ac8f1d2d2ba57ec2891f48d2/_i18n/en/resources/user-guides/mine-to-pool.md)
