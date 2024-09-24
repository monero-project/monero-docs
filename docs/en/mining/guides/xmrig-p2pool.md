---
title: How to mine on P2Pool with XMRig
---

### Pool Website

- P2Pool.io Main [Clearnet](https://p2pool.io) and [Onion](http://yucmgsbw7nknw7oi3bkuwudvc657g2xcqahhbjyewazusyytapqo4xid.onion/)
- P2Pool.io Mini [Clearnet](https://p2pool.io/mini) and [Onion](http://yucmgsbw7nknw7oi3bkuwudvc657g2xcqahhbjyewazusyytapqo4xid.onion/mini/)

### Observer (Miner Stats)
- Main [Clearnet](https://p2pool.observer/) and [Onion](http://p2pool2giz2r5cpqicajwoazjcxkfujxswtk3jolfk2ubilhrkqam2id.onion/)
- Mini [Clearnet](https://mini.p2pool.observer/) and [Onion](http://p2pmin25k4ei5bp3l6bpyoap6ogevrc35c3hcfue7zfetjpbhhshxdqd.onion/)

## Requirements
### Wallet

Before starting, you'll need to have a Monero Wallet configured.    
It's highly recommended to create a new wallet for mining because wallet addresses are public on p2pool.    
You have to use the Primary wallet address for mining.    
_Subaddresses and integrated addresses are not supported._

### Node

P2Pool requires access to a properly configured Monero node. If you have a Monero node you will need to add the following to your monerod config file or startup flags

    --zmq-pub tcp://127.0.0.1:18083

**Example**

    ./monerod --zmq-pub tcp://127.0.0.1:18083 --out-peers 32 --in-peers 64 --add-priority-node=p2pmd.xmrvsbeast.com:18080 --add-priority-node=nodes.hashvault.pro:18080 --disable-dns-checkpoints --enable-dns-blocklist

If you do not run your own node, you can still mine on P2Pool by using a public ZMQ node.<br>An easy method is to use [Gupax](../guides/gupax.md).


### XMRig and P2Pool

You/ll need to download 2 pieces of software: XMRig & P2Pool.

- You can download XMRig from: [XMRig.com](https://xmrig.com/download)
- You can download P2Pool from: [P2Pool GitHub Repo](https://github.com/SChernykh/p2pool/releases/latest)

Note that you should check for, and update   your P2Pool software regularly.

## Configuring P2Pool

1. Open port `37889` for P2Pool "Main" or `37888` for P2Pool "Mini" in your firewall to ensure better connectivity (Optional)
2. Run `./p2pool --host NODE_IP_ADDRESS --rpc-port NODE_RPC_PORT --wallet WALLET_ADDRESS`.

    - It's recommended that you use your own node. If that's the case `NODE_IP_ADDRESS` should be `127.0.0.1`.
    - Similarly, the `NODE_RPC_PORT` should be `18081` or `18089`.
    - `WALLET_ADDRESS` **must** be your main address. Subaddresses are unsupported. <br>(Main addresses start with `4`, subaddresses start with `8`)
    - Add the flag `--mini` if youd prefer to mine on a lower difficulty P2Pool instance.

3. Wait for P2Pool to synchronize. It should take no more than 5-10 minutes.

See the [official docs](https://github.com/SChernykh/p2pool/blob/master/docs/COMMAND_LINE.MD) for more details about P2Pool.

## Running XMRig

On Linux and MacOS etc, run `./xmrig -o 127.0.0.1:3333` to start mining.
For higher hashrates on Windows, you'll need to edit properties to run as administrator. On Linux you'll run with `sudo`.

See the [official docs](https://xmrig.com/docs/miner/config) if youd prefer to use a config file.

## Efficiency

You may want to check your efficiency before you start mining. This is based on your power costs vs the hashrates that your hardware is able to produce.
You can check your estimated hashrates at [xmrig.com/benchmark](https://xmrig.com/benchmark/).
There are many sites, such as [CryptoCompare](https://www.cryptocompare.com/mining/calculator/xmr/) that allow you to enter your hashrate, power draw and power costs to calculate your efficiency.

## Troubleshooting

### Anti-virus keeps removing XMRig

Some anti-viruses flag XMRig as malware because it is often deployed
to infected computers to mine without the owner's consent. As it is
your computer, and you are configuring the miner to mine for you, it is
safe to add XMRig and P2Pool to your anti-virus whitelist.

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

Firstly stop the miner (if it's running), run the following commands to enable large pages and then start the miner as root:

	sudo sysctl -w vm.nr_hugepages=1168
	sudo ./xmrig

You may have to increase 1168 depending on how many NUMA nodes your CPU(s) have.

#### Allowing large pages on macOS

Huge pages are not supported on macOS.

### Balance Not Increasing

P2Pool uses <abbr title="Pay Per Last N Shares">PPLNS</abbr> system, which means that you only get paid when a miner on the pool finds a Monero block.

## Getting Help

There is an active Monero mining community on Reddit at [/r/MoneroSupport](https://www.reddit.com/r/MoneroSupport/). You can
also join #monero-pools on [Libera](https://web.libera.chat/?channel=#monero-pools) or [Matrix](https://matrix.to/#/%23monero-pools:monero.social).