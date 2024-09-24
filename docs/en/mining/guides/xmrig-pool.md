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

There are numerous pools to choose from. You can find a list at[miningpoolstats.stream/monero](https://miningpoolstats.stream/monero).

Keep in mind that you should _not_ choose one of the top 3 pools.    
Choosing a smaller pools helps keep the network decentralised.    
Whatever pool you choose, be sure to pay attention to the pool's fees and the minimum withdrawal. You won't be able to withdraw your funds until you reach the pool's threshold. Each pool has their own minimums and fees.

## Configuring XMRig

The pool website will typically have instructions on how to setup and run XMRig.    
See the [official docs](https://xmrig.com/docs/miner/config) for instructions on setting up using a config file and further suggestions.

Start the miner using the parameters shown to you by the Pool's website.

If you see green messages saying that shares have been accepted,
congratulations, everything is working!

## Efficiency

You may want to check your efficiency before you start mining. This is based on your power costs vs the hashrates that your hardware is able to produce.    
You can check your estimated hashrates at [xmrig.com/benchmark](https://xmrig.com/benchmark/).    
There are many sites, such as [CryptoCompare](https://www.cryptocompare.com/mining/calculator/xmr/) that allow you to enter your hashrate, power draw and power costs to calculate your efficiency.
## Troubleshooting

### Anti-virus keeps removing XMRig

Some anti-viruses flag XMRig as malware because it is often deployed
to infected computers to mine without the owner's consent. As it is
your computer and you are configuring the miner to mine for you, it is
safe to add XMRig to your anti-virus whitelist.

### Cannot read/set MSR

On some CPUs, XMRig tries to increase performance by disabling certain
features like your CPU's instruction prefetcher. These operations
require root/administrator, so try right clicking xmrig.exe and
running it as administrator, or running with `sudo` on other
systems.

### Algo not known

Find the line in config.json that says `algo: null` and change it to
`algo: "rx/0"`. By default, XMRig expects the pool to tell it which
hashing algorithm to use.

### Huge Pages 0%

#### Allowing large pages on Windows

Taken from [the MSDN](https://docs.microsoft.com/en-us/sql/database-engine/configure-windows/enable-the-lock-pages-in-memory-option-windows?view=sql-server-ver15):

1. On the Start menu, click Run. In the Open box, type gpedit.msc.
2. On the Local Group Policy Editor console, expand Computer Configuration, and then expand Windows Settings.
3. Expand Security Settings, and then expand Local Policies.
4. Select the User Rights Assignment folder.
5. The policies will be displayed in the details pane.
6. In the pane, double-click Lock pages in memory.
7. In the Local Security Setting – Lock pages in memory dialog box, click Add User or Group.
8. In the Select Users, Service Accounts, or Groups dialog box, add an account that you will run the miner on
9. Reboot for change to take effect.

You may also need to launch the miner as administrator.

#### Allowing large pages on Linux

Firstly stop the miner (if it's running), run the following commands to enable
large pages and then start the miner as root:

	sudo sysctl -w vm.nr_hugepages=1168
	sudo ./xmrig

You may have to increase 1168 depending on how many NUMA nodes your
CPU(s) have.

#### Allowing large pages on macOS

Huge pages are not supported on macOS.

### Balance Not Increasing

Most pools are <abbr title="Pay Per Last N Shares">PPLNS</abbr> pools, which means that you only get paid when a miner on the pddool finds a block. If the pool you are mining on is small, this can take a few days to weeks.

Additionally, any blocks found must mature before they can be paid out. This takes 60 blocks (approx. 2 hours).

## Getting Help

There is an active Monero mining community on Reddit at [/r/MoneroSupport](https://www.reddit.com/r/MoneroSupport/). You can
also join #monero-pools on [Libera](https://web.libera.chat/?channel=#monero-pools) or [Matrix](https://matrix.to/#/%23monero-pools:monero.social).

## Going Further

* Consider using a subaddress just for mining, to prevent your address
  being linked to different services.
* [Consider using Tor to connect to the
  pool](https://xmrig.com/docs/miner/tor) (or to a hidden service pool
  like HashVault and MoneroOcean). This hides mining
  activity from your ISP, and prevents the pool from knowing who you
  are.

Adapted from [monero-site](https://github.com/monero-project/monero-site/commit/ee03c625e6257f25ac8f1d2d2ba57ec2891f48d2)