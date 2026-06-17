---
title: Running a Node
---
# Running a Monero Node

Running your own `monerod` node lets you interact with the Monero network
directly, without trusting a third-party remote node. The pages below cover
configuring, running as a service, and adding network privacy.

New to running a node? First [download](../interacting/download-monero-binaries.md)
and [verify](../interacting/verify-monero-binaries.md) the official software, then
use the guides below to configure and run it.

## Configure monerod

- [`monerod` Reference](../interacting/monerod-reference.md) - the command-line flags and options `monerod` accepts.
- [Monero Configuration File](../interacting/monero-config-file.md) - set those options in a config file instead of long command lines, with sample configs.

## Run it as a service

- [Running a Node via Systemd](./monerod-systemd.md) - keep `monerod` running in the background and start it on boot.

## Network privacy

- [Tor and I2P](./monerod-tori2p.md) - run your node over Tor and I2P for added privacy.
