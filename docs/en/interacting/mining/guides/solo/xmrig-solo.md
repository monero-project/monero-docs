---
title: How to solo mine with XMRig
---

## Requirements
### Wallet

Before starting, you'll need to have a Monero Wallet configured.

You have to use the Primary wallet address for mining - _Subaddresses and integrated addresses are not supported._

### Node

**Optional:** Solo mining using XMRig can be configured to use ZMQ to avoid polling the node. To use ZMQ instead of polling add the following to your monerod config file or startup flags:

    --zmq-pub tcp://127.0.0.1:18083

**Example**

    ./monerod --zmq-pub tcp://127.0.0.1:18083 --out-peers 32 --in-peers 64 --add-priority-node=p2pmd.xmrvsbeast.com:18080 --add-priority-node=nodes.hashvault.pro:18080 --disable-dns-checkpoints --enable-dns-blocklist


### XMRig

You'll need to download or compile XMRig.

You can download XMRig from: [XMRig.com](https://xmrig.com/download)

## Configuring XMRig

XMRig can be run using a config file or startup flags:

**Note:** remove the parameter for `daemon-zmq-port` if your node does not have it enabled.

=== "Config"
    There is a wizard on [XMRig.com](https://xmrig.com/wizard#result).

    Modify the pool section of your config file:
    ``` json
    "pools": [
        {
            "enabled": true,
            "url": "127.0.0.1:18081",
            "user": "XMR_WALLET_ADDRESS",
            "daemon": true,
            "daemon-zmq-port": 18083,
        }
    ],
    ```
    See the [official docs](https://xmrig.com/docs/miner/config).

=== "Flags"

    Add the following flags to your xmrig startup:

    ```
    --daemon -o 127.0.0.1:18081 -u XMR_WALLET_ADDRESS --daemon-zmq-port 18083
    ```

    See the [official docs](https://xmrig.com/docs/miner/command-line-options).

## Running XMRig

=== "Config"
    === "Linux / macOS"

        ```
        ./xmrig -c config.json
        ```
        For higher hashrates on Linux and macOS, you'll need to run with `sudo`.

    === "Windows"

        ```
        xmrig.exe -c config.json
        ```
        For higher hashrates on Windows, you'll need to edit properties to run as administrator


=== "Flags"
    === "Linux / macOS"

        ```
        ./xmrig --daemon -o 127.0.0.1:18081 -u XMR_WALLET_ADDRESS --daemon-zmq-port 18083
        ```
        For higher hashrates on Linux and macOS, you'll need to run with `sudo`.

    === "Windows"

        ```
        xmrig.exe --daemon -o 127.0.0.1:18081 -u XMR_WALLET_ADDRESS --daemon-zmq-port 18083
        ```
        For higher hashrates on Windows, you'll need to edit properties to run as administrator

{% include 'mining_footer' %}

Adapted from [monero-site](https://github.com/monero-project/monero-site/blob/ee03c625e6257f25ac8f1d2d2ba57ec2891f48d2/_i18n/en/resources/user-guides/mine-to-pool.md)
