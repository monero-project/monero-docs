---
title: Monero Configuration File

configfile: "~/.bitmonero/bitmonero.conf"
datadir: "~/.bitmonero"
logfile: "log-file=~/.bitmonero"
maxlogsize: ""
publicnode: "#public-node=1                  # Advertise to other users they can use this node for connecting their wallets"

---
# Monero Configuration File

## Applicability

By default Monero looks for `bitmonero.conf` in Monero [data directory](../interacting/overview.md#data-directory).

To use a specific config file add `--config-file` option:

`./monerod --config-file=/etc/monerod.conf`

The `--config-file` option is available for: 

- `monerod`
- `monero-wallet-cli`
- `monero-wallet-rpc`
- `monero-gen-trusted-multisig`

## Syntax

- `option-name=value`
- `valueless-option-name=1` for options that don't expect value
- `# comment`
- whitespace is ignored

## Reference

All configuration options are the same as command line options for the binary.

- [monerod reference](../interacting/monerod-reference.md)
- [monero-wallet-cli reference](../interacting/monero-wallet-cli-reference.md)
- [monero-wallet-rpc reference](../interacting/monero-wallet-rpc-reference.md)

Skip the `--` from `--option-name`.

Example:

`./monerod --log-level=4 --stagenet`

translates to:

```ini
log-level=4
stagenet=1     # use value "1" to enable the value-less options like --stagenet
```
## Templates

### `monerod.conf`

This config is tailored for desktop usage on [mainnet :link:](../infrastructure/networks.md#mainnet)
{% include 'monerod_template' %}

### `monero-wallet-cli.conf`

This config is tailored for desktop usage on [stagenet :link:](../infrastructure/networks.md#stagenet).

```ini
# ~/.bitmonero/stagenet/monero-wallet-cli.conf

# Pick network
stagenet=1

# Connect to a remote full node
daemon-address=YOUR.NODE.IP:38081
#trusted-daemon=1

# Log file
log-file=/tmp/monero-wallet-cli.log

# wallet-file=~/.bitmonero/stagenet/wallets/MoneroExampleStagenetWallet
```
