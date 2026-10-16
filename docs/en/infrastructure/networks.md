---
title: Mainnet, Stagenet, Testnet, Regtest
---
# Networks

!!! note ""
    Monero offers three distinct networks and blockchains, plus a local regression testing mode:

    [**mainnet**](#mainnet)    
    [**stagenet**](#stagenet)    
    [**testnet**](#testnet)    
    [**regtest**](#regtest)

     Every network has its own genesis block and is entirely separate from others.

## Nodes & Explorers

!!! danger "Spy Nodes and Explorers"
    Be cautious when using **_any_** remote node or block explorer.

    Malicious service providers may log and associate your IP address, TXIDs, and more.
    If you must use Untrusted Nodes, use them over Onion or I2P. See [Remote Nodes and Privacy](../interacting/remote-nodes.md) for the trade-offs.


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
    - [xmr.mx](http://ravfxexpx76quysu77pbvao4ng5qnyo46gguklfwlafhllrujwdgqtyd.onion/)

??? tip "Mainnet Block Explorers [I2P]"
    - [xmr.mx](http://ravfxexpucy437tc4slicbf5atir2akrcqanog3tgsc3mcdfmrqq.b32.i2p/)

??? danger "Mainnet Block Explorers [Clearnet]"
    - [Localmonero.co](https://localmonero.co/blocks/)
    - [monerowatch](https://monerowat.ch/)
    - [P2Pool.io](https://p2pool.io/explorer/)
    - [xmr.mx](https://explorer.xmr.mx/)
    - [XMRChain.net](https://xmrchain.net/)

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
    - [LibreNode.com](http://xmr-stagenet.gw3ennwsaonltfox7z3rhhof6mxcq2fnwhcj2qyp3kxsfldnxix5b4yd.onion/)

??? danger "Stagenet Block Explorers [Clearnet]"
    - [XMRChain.net](https://stagenet.xmrchain.net/)
    - [LibreNode.com](https://xmr-stagenet.librenode.com/)

??? tip "Stagenet Faucets [Onion]"
    - [CypherFaucet.com](https://afhhz7ytxc6en5qbcftugdt2yuxhnzxdhg6dpto67rkv75ofwgjwavid.onion/xmr-stagenet)

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
    If you're a normal user, you should use [Stagenet](#stagenet).

    If you're a developer building an application, you should use [Stagenet](#stagenet) for a live network, or [Regtest](#regtest) for a local one.

    Testnet is the "experimental" network and blockchain where things get tested long before mainnet.

    Testnet forks earlier and more often than Mainnet. To avoid being stuck on an old fork of testnet, you should keep your sources up to date and compile often.

Some resources to get started:

- Build Monero from source following a guide from [Monero Examples](https://github.com/moneroexamples/monero-compilation/)

??? tip "Testnet Block Explorers [Onion]"
    - [Monerodevs.org](http://ol7qm5adjeugpwkbrcnnnshsihmkhidaaoim35duhfdmj4gihaiapkid.onion/)
    - [LibreNode.com](http://xmr-testnet.gw3ennwsaonltfox7z3rhhof6mxcq2fnwhcj2qyp3kxsfldnxix5b4yd.onion/)

??? danger "Testnet Block Explorers [Clearnet]"
    - [XMRChain.net](https://testnet.xmrchain.net/)
    - [LibreNode.com](https://xmr-testnet.librenode.com/)

??? tip "Testnet Faucets [Onion]"
    - [CypherFaucet.com](https://afhhz7ytxc6en5qbcftugdt2yuxhnzxdhg6dpto67rkv75ofwgjwavid.onion/xmr-testnet)

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
    A private testnet follows the testnet hard fork table, so a new chain starts on hard fork version 1 and only reaches the current rules at the same heights as the public testnet, unless you modify the hard fork table and recompile.

    A private testnet is only recommended when you need to test hard fork boundaries, unreleased hard forks, or old transaction types. Otherwise, use [Regtest](#regtest).

    To learn how to run a private testnet, follow the guide from [Monero Examples](https://github.com/moneroexamples/private-testnet/)

## Regtest

!!! info ""
    Regtest is a local regression testing mode, ideal for third-party developers and CI runs. It is enabled by starting `monerod` with `--regtest`.

    Regtest starts a new, private chain that uses the latest hard fork rules from block 1.

    Regtest uses the mainnet address format. The chain is deleted on each start unless `--keep-fakechain` is passed.

??? tip "Start a Regtest node"
    `--offline` keeps the node from connecting to other peers, `--fixed-difficulty` keeps the difficulty constant so blocks can be generated quickly, and `--keep-fakechain` keeps the chain across restarts.

    ```bash
    monerod --regtest --offline --fixed-difficulty=1 --keep-fakechain
    ```

??? tip "Generate blocks"
    Blocks are created on demand, and the coinbase reward is paid to the given address.

    === "RPC"
        Use the [generateblocks](../rpc-library/monerod-rpc.md#generateblocks) RPC.

        ```bash title="Request"
        curl http://127.0.0.1:18081/json_rpc \
          -H 'Content-Type: application/json' \
          -d '{
            "jsonrpc": "2.0",
            "id": "0",
            "method": "generateblocks",
            "params": {
              "amount_of_blocks": 100,
              "wallet_address": "44AFFq5kSiGBoZ4NMDwYtN18obc8AemS33DBLWs3H7otXft3XjrpDtQGv7SqSsaBYBb98uNbr2VBBEt7f2wfn3RVGQBEP3A"
            }
          }'
        ```

    === "Interactive"
        Use the `generate_blocks <addr> <numblocks> [<starting_nonce>]` command in the `monerod` console.

        ```
        generate_blocks 44AFFq5kSiGBoZ4NMDwYtN18obc8AemS33DBLWs3H7otXft3XjrpDtQGv7SqSsaBYBb98uNbr2VBBEt7f2wfn3RVGQBEP3A 100
        ```

??? abstract "Regtest TCP ports"

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

## FAQ

??? question "Why do stagenet and testnet coins have no value?"

    A: This is simply the convention community embraced. Value only comes from a shared belief that mainnet coins will be accepted by other people in the future.
