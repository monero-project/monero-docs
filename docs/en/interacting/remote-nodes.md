---
title: Remote Nodes
---
# Remote Nodes and Privacy

Monero wallets do not store the blockchain itself; instead, they connect to a full or pruned node to scan the chain for incoming transactions. This node can run on your own machine (a local node) or on someone else's machine/server (a remote node).

Remote nodes can be convenient, as there is nothing large to download or keep synced. However, the trade-off is that you rely on a third party for your wallet's view of the blockchain, and that third party can potentially learn information about you.

!!! tip "Summary"
    Running your own node is not necessarily private on its own. To keep your transactions from being linked to your IP address, have it broadcast them over Tor or I2P with `--tx-proxy`, and ideally route the rest of its traffic through `--proxy` as well (see [Tor/I2P and proxies](monerod-reference.md#tori2p-and-proxies)). If you have to use a remote node, prefer one which you trust/control, and connect to it as a Tor or I2P hidden service. See the [comparison](#comparing-your-options) below.

## What a remote node cannot do

A remote node never receives your private keys or your wallet file, so it *cannot* do the following:

- spend or steal your funds
- create transactions on your behalf
- decrypt transaction amounts, or see your balance directly

The wallet application downloads blocks and scans them locally with your private view key. The node does not learn which outputs contained in those blocks actually belong to you just from serving them.

## What remote nodes can learn

- Your IP address
- The transactions you send (though much of the actual data is protected by Monero's cryptography)
- Which outputs your transactions spend from
- Which outputs you own, if you mark the node as trusted. Requests such as checking whether your key images are spent, or scanning for specific transactions, are only sent to a trusted node. Some wallets need a trusted node to work at all (for example, air-gapped wallets such as ANONERO and Cupcake), and so reveal your owned outputs to it.

## What a malicious remote node can do

Aside from logging, a dishonest node can interfere with your wallet in several ways:

- Refuse to relay transactions, or delay them
- Hide or withhold important data, such that incoming payments will appear late (or not at all)
- Return misleading data. Wallets do apply some sanity checks, but can't fully verify everything a node tells them. For example:
    - An inflated fee estimate, making you pay far more in fees than necessary. Always check the fee before confirming a transaction.
    - Biased ring decoys, in an attempt to weaken your ring signature privacy.

## Connection security

If you connect to a remote node over plain HTTP on the clearnet, anyone on the network path (such as your ISP, a public Wi-Fi network, or an attacker in between) can see all traffic that is sent, including the transactions you broadcast. They can also tamper with responses.

To avoid this, do the following:

- Connect over Tor or I2P. These connections are end-to-end encrypted, and also hide your IP address from the node.
- Otherwise, use SSL/TLS. `monerod` supports SSL/TLS on its RPC port (`--rpc-ssl`, see the [`monerod` reference](monerod-reference.md#node-rpc-api)). For a node you run yourself, you can pin its certificate in the wallet with `--daemon-ssl-allowed-fingerprints` (see the [`monero-wallet-rpc` reference](monero-wallet-rpc-reference.md#daemon-node)).

## Comparing your options

From most to least private:

| Setup | Who can link your transactions to your IP | Notes
|-------|-------------------------------------------|------
| Local node with `--proxy` and `--tx-proxy` | Nobody | All of the node's P2P traffic goes over the specified `--proxy`, and your own transactions are broadcast over an anonymity network.
| Local node with `--tx-proxy` | Nobody | Your own transactions are broadcast over Tor/I2P. Other traffic (such as syncing blocks) uses the clearnet, so peers can see that your IP runs a node.
| Remote node via hidden service (Tor or I2P) | Nobody | The node operator sees your transactions, but not your IP. This includes your own node reached remotely; see [Wallet Setup](../running-node/monerod-tori2p.md#wallet-setup).
| Remote (clearnet) node via Tor | Nobody | The node operator sees your transactions, but not your IP. Without SSL/TLS, the Tor exit relay can also see and tamper with your traffic.
| Remote node via VPN | The VPN provider | The node operator only sees the VPN's IP address. The VPN provider sees your real IP, and without SSL/TLS, your traffic too.
| Remote node with SSL/TLS | The node operator | Others on the network path can't read your traffic, but the operator sees your IP and the transactions you send.
| Local node without an anonymity network (the default) | Potentially, your peers | Your transactions are broadcast over the clearnet. Dandelion++ makes their origin harder to trace, but does not protect against the first node they are sent to.
| Remote node without SSL/TLS | The node operator, and anyone on the network path | Least private, avoid when possible.

!!! note
    If you run a local node with `--tx-proxy`, also enabling `--anonymous-inbound` adds plausible deniability; your node will relay transactions received from Tor/I2P peers to the clearnet, so to an outside observer these appear to originate from your node, just like your own would. See the [Tor/I2P setup guide](../running-node/monerod-tori2p.md).

Running a local node needs about {{ lmdb_size_pruned }} GiB of disk for a pruned node, as of {{ lmdb_size_updated }}.
