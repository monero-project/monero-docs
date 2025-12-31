---
title: Troubleshooting
---
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

Most pools (including P2Pool) use <abbr title="Pay Per Last N Shares">PPLNS</abbr> system.

- [**Solo Mining**](./solo/index.md): you will only get paid when you mine a block.
- [**P2Pool**](./p2pool/xmrig-p2pool.md): you will only get paid when a miner on the pool finds a Monero block and you have a share within the PPLNS window.
- [**Traditional Pool**](./pool/xmrig-pool.md): you will you get paid then you meet the pool's payout threshold.

## Getting Help

There is an active Monero mining community on Reddit at [/r/MoneroMining](https://www.reddit.com/r/MoneroMining/). You can
also join on Libera at [#monero-mining](https://web.libera.chat/#monero-mining) or on Matrix at [#xmrmine](https://matrix.to/#/%23xmrmine:matrix.org).
