---
title: monero-wallet-rpc - Reference
---

# `monero-wallet-rpc` - Reference

!!! note
    This is only relevant for programmers. Everyday users won't need `monero-wallet-rpc`.

!!! note
    Use [stagenet](../infrastructure/networks.md) for learning and development on top of `monero-wallet-rpc`.

## JSON-RPC interface

For a list of `monero-wallet-rpc` calls, their inputs, outputs, and examples, visit the wallet-rpc [library](../rpc-library/wallet-rpc.md)

## Overview

### Provides wallet API over HTTP

Programmers can build thin user interfaces (UIs) on top of `monero-wallet-rpc`.

Programmers can also use `monero-wallet-rpc` to build arbitrary wallet automation driven by HTTP calls.

Think of `monero-wallet-rpc` as complete wallet logic exposed via JSON-RPC over HTTP.

Wallet uses your private keys to understand your total balance,
transactions history, and to facilitate creating transactions.

However, wallet does not store the blockchain and does not directly participate in the p2p network.

### Depends on the full node

Wallet connects to a [full node](../interacting/monerod-reference.md) to scan the blockchain for your transaction outputs and to send your transactions out to the network.

The full node can be either local (same computer) or remote.

You can play with [CLI wallet](../interacting/monero-wallet-cli-reference.md) and [GUI wallet](../interacting/monero-wallet-gui-reference.md) first to understand the relationship between the full node, the wallet and the user.

## Syntax

`./monero-wallet-rpc --rpc-bind-port <port> (--wallet-file <file>|--generate-from-json <file>|--wallet-dir <directory>) [options]`

Or with a config file:

`./monero-wallet-rpc --config-file <arg>`

## Running

Make sure you are running a locally synced `monerod` or point to a remote daemon with `--daemon-address` option.

#### Linux (Production Example)

`./monero-wallet-rpc --rpc-bind-port 28088 --wallet-file wallets/main/main --password walletPassword --rpc-login monero:rpcPassword --log-file logs/monero-wallet-rpc.log --max-log-files 2 --trusted-daemon`

- If the RPC is used to retrieve information not dependent on any spending, consider using a view-only to prevent abuse.
- `--rpc-login` should be used in production to protect against unauthorized access.

#### Windows (Development Example)

`monero-wallet-rpc --rpc-bind-port 28088 --wallet-file wallets\main\main --password walletPassword --daemon-address http://node.supportxmr.com:18081 --untrusted-daemon --disable-rpc-login`

- Specifying `--untrusted-daemon` is not necessary but tells yourself that the daemon is untrusted and that commands requiring a trusted daemon will be disabled
- Default installation on Windows is `"C:\Program Files\Monero GUI Wallet"`

### Trouble Shooting

If the expected RPC URL, say [http://127.0.0.1:28088/json_rpc](http://127.0.0.1:28088/json_rpc), is unavailabe, or there is no terminal output saying that the server has been started, `monero-wallet-rpc` might be trying to synchronize the wallet. In that case, you should use the GUI or CLI to sync that wallet file because using the GUI/CLI results in faster and measurable syncing.

The suggested way is to have two wallet files for the same keys. One that is used manually (synced often), and one that is used by `monero-wallet-rpc`. Whenever you decide to use `monero-wallet-rpc` and encounter the unresponsive issue, simply copy the files of the GUI/CLI wallet and replace the ones that were being used by `monero-wallet-rpc`. This problem should only occur on the development system where `monerod` or `monero-wallet-rpc` might not have been running for weeks. In production, `monerod` and `monero-wallet-rpc` should have minimal downtimes, ensuring that the wallet is always synchronized.

## Options

### Help and Version

| Option       | Description
|--------------|------------
|  `--help`    | Produce help message
|  `--version` | Output version information

### Pick Network

| Option        | Description
|---------------|------------
|  `--testnet`  | For testnet. Daemon must also be launched with --testnet flag
|  `--stagenet` | For stagenet. Daemon must also be launched with --stagenet flag

### Logging

| Option                                 | Description
|----------------------------------------|------------
|  `--log-file <arg>`                    | Specify log file
|  `--log-level <arg>`                   | 0-4 or categories<br><br>(=0)
|  `--max-log-file-size <arg>`           | Specify maximum log file size in bytes<br><br>(=104850000)
|  `--max-log-files <arg>`            | Specify maximum number of rotated log files to be saved (no limit by setting to 0)<br><br>(=10)

### Daemon (Node)

| Option                                     | Description
|--------------------------------------------|-----
|  `--daemon-address <arg>`                  | Use daemon instance at `<host>:<port>`
|  `--daemon-host <arg>`                     | Use daemon instance at host `<arg>` instead of localhost
|  `--proxy <arg>`                           | `[<ip>:]<port>` socks proxy to use for daemon connections
|  `--trusted-daemon`                        | Enable commands which rely on a trusted daemon
|  `--untrusted-daemon`                      | Disable commands which rely on a trusted daemon
|  `--password <arg>`                        | Wallet password (escape/quote as \| needed)
|  `--password-file <arg>`                   | Wallet password file
|  `--daemon-port <arg>`                     | Use daemon instance at port `<arg>` instead of 18081
|  `--daemon-login <arg>`                    | Specify username[:password] for daemon RPC client
|  `--daemon-ssl <arg>`                      | Enable SSL on daemon RPC connections: enabled\|disabled\|autodetect<br><br>(=autodetect)
|  `--daemon-ssl-private-key <arg>`          | Path to a PEM format private key
|  `--daemon-ssl-certificate <arg>`          | Path to a PEM format certificate
|  `--daemon-ssl-ca-certificates <arg>`      | Path to file containing concatenated PEM format certificate(s) to replace system CA(s).
|  `--daemon-ssl-allowed-fingerprints <arg>` | List of valid fingerprints of allowed RPC servers
|  `--daemon-ssl-allow-any-cert`             | Allow any SSL certificate from the daemon
|  `--daemon-ssl-allow-chained`              | Allow user (via --daemon-ssl-ca-certificates) chain certificates

### Other Useful

| Option                | Description
|-----------------------|-----
| `--tx-notify <arg>`   | Run a program for each new incoming transaction, '%s' will be replaced by the transaction hash
| `--detach`            | Fork to the background
| `--pidfile` <arg>     | Store the PID inside of a file. Requires `--detach`
| `--config-file <arg>` | Config file

### RPC

| Option                                          | Description
|-------------------------------------------------|-----
|  `--rpc-bind-port <arg>`                        | Sets bind port for server
|  `--disable-rpc-login`                          | Disable HTTP authentication for RPC connections served by this process
|  `--restricted-rpc`                             | Restricts to view-only commands
|  `--rpc-bind-ip <arg>`                          | Specify IP to bind RPC server<br><br>(=127.0.0.1)
|  `--rpc-bind-ipv6-address <arg>`                | Specify IPv6 address to bind RPC server<br><br>(=::1)
|  `--rpc-restricted-bind-ip <arg>`               | Specify IP to bind restricted RPC server<br><br>(=127.0.0.1)
|  `--rpc-restricted-bind-ipv6-address <arg>`     | Specify IPv6 address to bind restricted RPC server<br><br>(=::1)
|  `--rpc-use-ipv6`                               | Allow IPv6 for RPC
|  `--rpc-ignore-ipv4`                            | Ignore unsuccessful IPv4 bind for RPC
|  `--rpc-login <arg>`                            | Specify username[:password] required for RPC server
|  `--confirm-external-bind`                      | Confirm rpc-bind-ip value is NOT a loopback (local) IP
|  `--rpc-access-control-origins <arg>`           | Specify a comma separated list of origins to allow cross origin resource sharing
|  `--rpc-max-connections <arg>`                  | Maximum number of RPC connections.<br><br>(=100)
|  `--rpc-max-connections-per-public-ip <arg>`    | Maximum number of RPC connections from the same public IP address.<br><br>(=3)
|  `--rpc-max-connections-per-private-ip <arg>`   | Maximum number of RPC connections from the same private IP address.<br><br>(=25)
|  `--rpc-response-soft-limit <arg>`              | Maximum response bytes that can be queued, enforced at next response attempt.<br><br>(=26214400)
|  `--rpc-ssl <arg>`                              | Enable SSL on RPC connections: enabled\|disabled\|autodetect<br><br>(=autodetect)
|  `--rpc-ssl-private-key <arg>`                  | Path to a PEM format private key
|  `--rpc-ssl-certificate <arg>`                  | Path to a PEM format certificate
|  `--rpc-ssl-ca-certificates <arg>`              | Path to file containing concatenated PEM format certificate(s) to replace system CA(s).
|  `--rpc-ssl-allowed-fingerprints <arg>`         | List of certificate fingerprints to allow
|  `--rpc-ssl-allow-chained`                      | Allow user (via --rpc-ssl-certificates) chain certificates
|  `--disable-rpc-ban`                            | Do not ban hosts on RPC errors
|  `--rpc-client-secret-key <arg>`                | Set RPC client secret key for RPC payments

### Open Existing Wallet

| Option                      | Description
|-----------------------------|-----
| `--wallet-file <arg>`       | Path to wallet. including filename
| `--wallet-dir <arg>`        | Directory to create, store and access wallets
| `--prompt-for-password`     | Prompts for password when not provided
| `--max-concurrency <arg>`   | Max number of threads to use for a parallel job<br><br>(=0)

### Create new Wallet

| Option                         | Description
|--------------------------------|-----
| `--kdf-rounds <arg>`           | (Not recommended) Number of rounds for the key derivation function<br><br>(=1)
| `--hw-device <arg>`            | HW device to use
| `--hw-device-deriv-path <arg>` | HW device wallet derivation path (e.g., SLIP-10)
| `--extra-entropy <arg>`        | File containing extra entropy to initialize the PRNG (any data, aim for 256 bits of entropy to be useful, which typically means more than 256 its of data)
| `--generate-from-json <arg>`   | Generate wallet from JSON format file

### Windows Service

| Option                 | Description
|------------------------|-----
|  `--run-as-service`    | true if running as windows service
|  `--install-service`   | Install Windows service
|  `--uninstall-service` | Uninstall Windows service
|  `--start-service`     | Start Windows service
|  `--stop-service`      | Stop Windows service

### Legacy and Rare Uses

| Option                                              | Description
|-----------------------------------------------------|-----
| `--shared-ringdb-dir <arg>`                         | Set shared ring database path<br>Windows: C:\ProgramData\.shared-ringdb<br>Linux: $HOME/.shared-ringdb
| `--no-dns`                                          | Do not use DNS
| `--offline`                                         | Do not connect to a daemon, nor use DNS
| `--non-interactive`                                 | monero-wallet-rpc is not interactive, this doesnt _do_ anything. [ref](https://github.com/monero-project/monero/pull/8772#issuecomment-1463097268)
| `--bitmessage-address <arg=http://localhost:8442/>` | Use PyBitmessage instance at URL `<arg>`
| `--bitmessage-login <arg>`                          | Specify `<arg>` as `username:password` for PyBitmessage API
