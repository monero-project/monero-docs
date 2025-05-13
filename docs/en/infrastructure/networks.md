---
title: Mainnet, Stagenet, Testnet
---
# Networks

!!! note ""
    Monero offers three distinct networks and blockchains:

    [**mainnet**](#mainnet)    
    [**stagenet**](#stagenet)    
    [**testnet**](#testnet)    

     Every network has its own genesis block and is entirely seperate from others.

## Nodes & Explorers

!!! danger "Spy Nodes and Explorers"
    Be cautious when using **_any_** remote node or block explorer.

    Malicious service providers may log and associate your IP address, TXIDs, and more.
    If you must use Untrusted Nodes, use them over Onion or I2P.


### Nodes

- Nodes - Self-Hosted
    - Run your own [node](../interacting/download-monero-binaries.md)
    - Use a node which is controlled by somebody you trust

- Nodes - Remote (Use an Onion or I2P node)
    - Onion and I2P nodes @ [monero.fail](https://monero.fail/)
    - Onion nodes @ [ditatompel.com](https://xmr.ditatompel.com/remote-nodes/)

### Block Explorers - Self-Hosted

- [Onion Monero Blockchain Explorer](https://github.com/moneroexamples/onion-monero-blockchain-explorer/)
- [MoneroBlock](https://github.com/duggavo/MoneroBlock/)


## Mainnet

!!! info ""
    Mainnet is the "production" network and blockchain.

    Mainnet is the only blockchain where XMR units have value.

    Mainnet is the default network.

??? tip "Mainnet Block Explorers [Onion]"
    - [P2Pool.io](http://yucmgsbw7nknw7oi3bkuwudvc657g2xcqahhbjyewazusyytapqo4xid.onion/explorer/)

??? danger "Mainnet Block Explorers [Clearnet]"
    - [P2Pool.io](https://p2pool.io/explorer/)
    - [XMRChain.net](https://xmrchain.net/)
    - [Localmonero.co](https://localmonero.co/blocks/)
    - [ExploreMonero.com](https://www.exploremonero.com/)

??? failure "Mainnet Faucets"
    - None. Don't fall for scams

??? abstract "Mainnet TCP ports"

    - 18080 - [Default] P2P Network
    - 18081 - [Default] Unrestricted [JSON-RPC](../rpc-library/monerod-rpc.md)
    - 18082 - [Default] ZMQ RPC
    - 18083 - ZMQ Pub
    - 18084 - Tor P2P
    - 18085 - I2P P2P
    - 18086 - Unused
    - 18087 - Unused
    - 18088 - [Wallet RPC](../interacting/monero-wallet-rpc-reference.md)
    - 18089 - Restricted [JSON-RPC](../rpc-library/monerod-rpc.md)

## Stagenet

!!! info ""
    Stagenet is available for users and developers to learn and build on Monero safely.

    Stagenet is technically equivalent to mainnet, both in terms of features and consensus rules. Similar to mainnet, you'll use the [latest official Monero release](https://getmonero.org/downloads/) to be compatible with stagenet.

Some resources to get started:

??? tip "Stagenet  Block Explorers [Onion]"
    - [Monerodevs.org](http://bhqzadcvfcuwwnvf5hws5zwzjgvfuarqbah5ruhyxuxhaoklsy35wdqd.onion/)

??? danger "Stagenet Block Explorers [Clearnet]"
    - [XMRChain.net](https://stagenet.xmrchain.net/)

??? abstract "Stagenet Faucets [Clearnet]"
    - [XMR-TW.org](https://stagenet-faucet.xmr-tw.org/)
    - [CypherFaucet.com](https://cypherfaucet.com/xmr-stagenet)

??? abstract "Stagenet TCP ports"

    - 38080 - [Default] P2P Network
    - 38081 - [Default] Unrestricted [JSON-RPC](../rpc-library/monerod-rpc.md)
    - 38082 - [Default] ZMQ RPC
    - 38083 - ZMQ Pub
    - 38084 - Tor P2P
    - 38085 - I2P P2P
    - 38086 - Unused
    - 38087 - Unused
    - 38088 - [Wallet RPC](../interacting/monero-wallet-rpc-reference.md)
    - 38089 - Restricted [JSON-RPC](../rpc-library/monerod-rpc.md)

Stagenet was introduced in March 2018 as part of Monero v0.12.0.0

## Testnet

!!! info ""
    If you're a normal user or a developer building an application, you should use [Stagenet](#stagenet).

    Testnet is the "experimental" network and blockchain where things get tested long before mainnet.

    Testnet forks earlier and more often than Mainnet. To avoid being stuck on an old fork of testnet, you should keep your sources up to date and compile often.

Some resources to get started:

- Build Monero from source following a guide from [Monero Examples](https://github.com/moneroexamples/monero-compilation/)

??? tip "Testnet Block Explorers [Onion]"
    - [Monerodevs.org](http://ol7qm5adjeugpwkbrcnnnshsihmkhidaaoim35duhfdmj4gihaiapkid.onion/)

??? danger "Testnet Block Explorers [Clearnet]"
    - [XMRChain.net](https://testnet.xmrchain.net/)

??? abstract "Testnet Faucets [Clearnet]"
    - [CypherFaucet.com](https://cypherfaucet.com/xmr-testnet)

??? abstract "Testnet TCP ports"

    - 28080 - [Default] P2P Network
    - 28081 - [Default] Unrestricted [JSON-RPC](../rpc-library/monerod-rpc.md)
    - 28082 - [Default] ZMQ RPC
    - 28083 - ZMQ Pub
    - 28084 - Tor P2P
    - 28085 - I2P P2P
    - 28086 - Unused
    - 28087 - Unused
    - 28088 - [Wallet RPC](../interacting/monero-wallet-rpc-reference.md)
    - 28089 - Restricted [JSON-RPC](../rpc-library/monerod-rpc.md)

### Private Testnet
??? info "Run a Private Testnet"

    You can create a private version of the Testnet.    
    A private testnet gives developers flexibility and control over the network.

    To learn how to run a private testnet, follow the guide from [Monero Examples](https://github.com/moneroexamples/private-testnet/)

## FAQ

??? question "Why do stagenet and testnet coins have no value?"

    A: This is simply the convention community embraced. Value only comes from a shared belief that mainnet coins will be accepted by other people in the future.
