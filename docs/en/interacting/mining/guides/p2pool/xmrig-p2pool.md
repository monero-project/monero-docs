---
title: How to mine on P2Pool with XMRig
---

### Pool Website

- P2Pool.io Main [Clearnet](https://p2pool.io) and [Onion](http://yucmgsbw7nknw7oi3bkuwudvc657g2xcqahhbjyewazusyytapqo4xid.onion/)
- P2Pool.io Mini [Clearnet](https://p2pool.io/mini) and [Onion](http://yucmgsbw7nknw7oi3bkuwudvc657g2xcqahhbjyewazusyytapqo4xid.onion/mini/)
- P2Pool.io Nano [Clearnet](https://p2pool.io/nano) and [Onion](http://yucmgsbw7nknw7oi3bkuwudvc657g2xcqahhbjyewazusyytapqo4xid.onion/nano/)

### Observer (Miner Stats)
- Main [Clearnet](https://p2pool.observer/) and [Onion](http://p2pool2giz2r5cpqicajwoazjcxkfujxswtk3jolfk2ubilhrkqam2id.onion/)
- Mini [Clearnet](https://mini.p2pool.observer/) and [Onion](http://p2pmin25k4ei5bp3l6bpyoap6ogevrc35c3hcfue7zfetjpbhhshxdqd.onion/)
- Nano [Clearnet](https://nano.p2pool.observer/) and [Onion](http://p2pnanphwyo2smf3khhjjkmfxll7h2ptmj4iwrbjklsk2wx66m5m7oad.onion/)

## Gupax (P2Pool GUI)
Gupax bundles P2Pool and XMRig into a single app with simple setup.

- Visit [Gupax](https://gupax.io).

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


### XMRig and P2Pool

You'll need to download 2 pieces of software: XMRig & P2Pool.

- You can download XMRig from: [XMRig.com](https://xmrig.com/download)
- You can download P2Pool from: [P2Pool GitHub Repo](https://github.com/SChernykh/p2pool/releases/latest)

Note that you should update your P2Pool software regularly.

## Configuring P2Pool

1. Open port `37889` for P2Pool "Main", `37888` for P2Pool "Mini", or `37890` for P2Pool "Nano" in your firewall to ensure better connectivity (Optional)
2. Run `./p2pool --host NODE_IP_ADDRESS --rpc-port NODE_RPC_PORT --wallet PRIMARY_WALLET_ADDRESS`.

    - It's recommended that you use your own node. If that's the case `NODE_IP_ADDRESS` should be `127.0.0.1`.
    - Similarly, the `NODE_RPC_PORT` should be `18081` or `18089`.
    - `PRIMARY_WALLET_ADDRESS` **must** be your main address. Subaddresses are unsupported. <br>(Main addresses start with `4`, subaddresses start with `8`)
    - Add the flag `--mini` if youd prefer to mine on a lower difficulty P2Pool instance.

3. Wait for P2Pool to synchronize. It should take no more than 5-10 minutes.

See the [official docs](https://github.com/SChernykh/p2pool/blob/master/docs/COMMAND_LINE.MD) for more details about P2Pool.

## Running XMRig

On Linux and MacOS etc, run `./xmrig -o 127.0.0.1:3333` to start mining.
For higher hashrates on Windows, you'll need to edit properties to run as administrator. On Linux you'll run with `sudo`.

See the [official docs](https://xmrig.com/docs/miner/config) if youd prefer to use a config file.

{% include 'mining_footer' %}

Adapted from [monero-site](https://github.com/monero-project/monero-site/blob/ee03c625e6257f25ac8f1d2d2ba57ec2891f48d2/_i18n/en/resources/user-guides/mine-to-pool.md)
