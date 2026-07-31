---
title: Tor and I2P

config: (../interacting/monero-config-file.md#monerodconf)
---

!!! note ""
    How to add Tor and/or I2P to your Monero node

### Assumptions

You possess:

- Basic understanding of Linux administration
- Root access to a Linux distribution
- A Monero Node

Some commands assume Ubuntu but you can trivially translate them to your distribution.

??? question "Why use anonymity networks?"

    **Why use anonymity networks?**
    You will be able to connect your desktop and mobile Monero wallets to your own trusted Monero node,
    in a secure and private way over Tor or I2P.

    **Tor and I2P hidden services for wallet interface** are useful for wallet users because it bypasses [NAT](https://tailscale.com/blog/how-nat-traversal-works) and also works to mitigate MITM risks (which are very real). Hidden service connections are end-to-end encrypted and private by default.

    **Onion and I2P for P2P network** is useful for other nodes as it allows them to relay transactions to your node (using `--tx-proxy` option).

??? question "What is the difference between I2P SOCKS and SAM?"

    SOCKS is a one-size-fits-all approach that makes use of i2pd server tunnels and a SOCKS5 proxy; this requires manual configuration of tunnels and may result in some [metadata leakage](https://i2p.net/en/docs/api/socks/).

    SAM (Simple Anonymous Messaging) is a protocol that lets `monerod` manage its own I2P connections directly, with no manual setup required aside from having an I2P router running. This is the recommended way to run the Monero daemon over I2P.

    However, at present, only SOCKS can be used for connecting to remote nodes from wallet software. SAM can still be used in conjunction with a full local node.

### Node Configuration
=== "Tor"
{% include 'tor_template' %}

=== "I2P SOCKS"
{% include 'i2pd_template' %}

=== "I2P SAM"
{% include 'i2pd_sam_template' %}

!!! note "(Optional) Publish the node on [monero.fail](https://monero.fail)"

## Wallet Setup

To connect Monero nodes, you have to configure the wallet software:
=== "Tor"
    === "Monero GUI"

        1. Navigate to: `Settings -> Interface -> Socks5 proxy` and set the values to `IP Address = 127.0.0.1` and `Port = 9050`
        2. Navigate to: `Settings -> Node -> Add remote node` and set the values to `Address = http://yourlongv3onionaddress.onion` and `Port = 18089`

        [:link: _Monero GUI_](../interacting/monero-wallet-gui-reference.md)

    === "Monero CLI"

        Add the flags `--proxy=127.0.0.1:9050 --daemon-address=http://yourlongv3onionaddress.onion:18089 --trusted-daemon`

        [:link: _Monero CLI_](../interacting/monero-wallet-cli-reference.md)

=== "I2P SOCKS"
    === "Monero GUI"

        1. Navigate to: `Settings -> Interface -> Socks5 proxy` and set the values to `IP Address = 127.0.0.1` and `Port = 4447`
        2. Navigate to: `Settings -> Node -> Add remote node` and set the values to `Address = http://yourlongb32i2paddress.b32.i2p` and `Port = 18089`

        [:link: _Monero GUI_](../interacting/monero-wallet-gui-reference.md)

    === "Monero CLI"

        Add the flags `--proxy=127.0.0.1:4447 --daemon-address=http://yourlongb32i2paddress.b32.i2p:18089 --trusted-daemon`

        [:link: _Monero CLI_](../interacting/monero-wallet-cli-reference.md)

=== "I2P SAM"
    === "Monero GUI"

        If using a local node managed through the GUI, go to Settings > Networks (in 'Advanced' mode) and ensure the 'I2P' anonymity network option is checked. Upon restarting the daemon, transactions will be forwarded over I2P.

        [:link: _Monero GUI_](../interacting/monero-wallet-gui-reference.md)
