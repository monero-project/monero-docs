---
title: Running Monero Open Node with Tor Onion Support
---
# Running Monero Open Node + Tor Onion

!!! success "The end goal"
    You will publicly offer the following services, where xxx.yyy.zzz.vvv is your server IP address.

    * xxx.yyy.zzz.vvv:18080 - clearnet P2P service (for other nodes)
    * xxx.yyy.zzz.vvv:18089 - clearnet RPC service (for wallets)
    * yourlongv3onionaddress.onion:18084 - onion P2P service (for other onion nodes)
    * yourlongv3onionaddress.onion:18089 - onion RPC service (for wallets connecting over Tor)

??? info "P2P ports"
    Q: Why different P2P ports for clearnet and onion?    
    A: The data served by the Onion differs from clearnet P2P. A different port is required

??? warning "May be resource intensive"
    Providing a Public RPC may use a sizeable amount of resources on your PC.

    If you have concerns about data/bandwidth, CPU or RAM usage, you may disable the `public-node` setting by commenting [#] or deleting the line from the [config](#config) 

## Why run this specific setup?

You will be able to connect your desktop and mobile Monero wallets to your own trusted Monero node,
in a secure and private way over Tor.

**Running as a systemd service** will allow your node to always remain synced, as opposed to intermittently running node.

**Serving blocks and transactions** in Monero P2P network helps new users to bootstrap and sync up their nodes.
It also strenghtens Monero P2P network against DDoS attacks and network partitioning.

**Open wallet inteface** - The `public-node` config option allows anyone to connect their wallets to Monero network through your node.
This is useful to users who don't run their own nodes.

**Tor onion for wallet interface** is useful for wallet users connecting over Tor because it mitigates Clearnet and Tor exit node MiTM risks (which are very real). By connecting wallet to an onion service, no MiTM attack is realistic because onion connections are end-to-end encrypted.

**Tor onion for P2P network** is useful for other full node users as it allows them to broadcast transactions over Tor (using `--tx-proxy` option).

## Assumptions

You possess:

- Basic understanding of Linux administration
- Root access to a Linux server
- _Recommended_ 4 GB+ RAM
- _Recommended_ available SSD storage of
    - **{{ multiply(lmdb_size_full, 2.5) }} GB+** for the full node
    - **{{ multiply(lmdb_size_pruned, 2.5) }} GB+** for the pruned.

!!! note "Current blockchain size as of {{ lmdb_size_updated }}"
    The current blockchain sizes are approximately:    
    Full node: **{{ lmdb_size_full }} GB**    
    Pruned node: **{{ lmdb_size_pruned }} GB**

Some commands assume Ubuntu but you will easily translate them to your distribution.

## Install Tor

1. [Install Tor](https://support.torproject.org/apt)

2. Elevate to root:

    ``` Bash
    sudo su -
    ```

3. Add the following lines to `/etc/tor/torrc`:

    ``` ApacheConf
    HiddenServiceDir /var/lib/tor/monerod
    HiddenServicePort 18089 127.0.0.1:18089    # interface for wallet ("RPC")
    HiddenServicePort 18084 127.0.0.1:18084    # interface for P2P network
    ```

4. Enable tor service:

    ``` Bash
    systemctl enable tor
    systemctl restart tor
    ```

5. Verify the Tor is running:

    ``` Bash
    systemctl status tor@default
    ```

6. View/Copy your new Onion Address: 

    ``` Bash
    cat /var/lib/tor/monerod/hostname
    ```

??? info "Backup Onion keys"
    You may want to backup your keys folder (`/var/lib/tor/monerod`) to secure control over your onion address.

??? info "How Tor onion services work?"

    A fresh onion address and corresponding key pair were created for you in /var/lib/tor/monero/.

    This happens on restart whenever you add a new `HiddenServiceDir` to the `/etc/tor/torrc` config file.

    The tor daemon will forward traffic from a virtual onion port to an actual localhost port, where some service is listening (in our case, this will be `monerod`).

    A single onion address can offer multiple services at various virtual ports.

## Install Monero

1. Create `monero` user and group:

    ``` Bash
    useradd --system monero
    ```

2. Create monero **config**, **data** and **log** directories:

    ``` Bash
    mkdir -p /etc/monero     # config
    mkdir -p /var/lib/monero # blockchain
    mkdir -p /var/log/monero # logs
    chown monero:monero /etc/monero
    chown monero:monero /var/lib/monero
    chown monero:monero /var/log/monero
    ```

    Feel free to adjust above to your preferred conventions, just remember to adjust the paths in the `systemd` and `monerod` config files accordingly.

3. [Download](../interacting/download-monero-binaries.md) and [verify](../interacting/verify-monero-binaries.md) the archive.

4. Extract the binaries (adjust filename if necessary):

    ``` Bash
    tar -xvf monero-linux-x64-{{ cli_vers }}.tar.bz2
    rm monero-linux-x64-{{ cli_vers }}.tar.bz2
    ```

5. Move binaries to /usr/local/bin/:

    ``` Bash
    mv monero-x86_64-linux-gnu-{{ cli_vers }}/* /usr/local/bin/.
    chown monero:monero /usr/local/bin/monero*
    ```

    ### **Monerod Config**

6. Create `/etc/monero/monerod.conf` as shown below and **replace `PASTE_YOUR_ONION_HOSTNAME` with your Onion address**.

    ``` YAML
    # /etc/monero/monerod.conf
    #
    # Configuration file for monerod. For all available options see the MoneroDocs:
    # https://docs.getmonero.org/interacting/monerod-reference/

    # Data directory (blockchain db and indices)
    data-dir=/var/lib/monero/bitmonero

    # Optional pruning
    #prune-blockchain=1           # Pruning saves 2/3 of disk space w/o degrading functionality but contributes less to the network
    #sync-pruned-blocks=1         # Allow downloading pruned blocks instead of prunning them yourself

    # Centralized services
    check-updates=disabled         # Do not check DNS TXT records for a new version
    enable-dns-blocklist           # Block known malicious nodes

    # Log file
    log-file=/var/log/monero/monero.log
    log-level=0                    # Minimal logs, WILL NOT log peers or wallets connecting
    max-log-file-size=2147483648   # Set to 2GB to mitigate log trimming by monerod; configure logrotate instead

    # P2P full node
    #p2p-bind-ip=0.0.0.0            # Bind to all interfaces (the default)
    #p2p-bind-port=18080            # Bind to default port
    #no-igd=1                       # Disable UPnP port mapping

    # RPC open node
    public-node=1                  # Advertise to other users they can use this node for connecting their wallets
    rpc-restricted-bind-ip=0.0.0.0 # Bind to all interfaces (the Open Node)
    rpc-restricted-bind-port=18089 # Bind to a new RESTICTED port (the Open Node)

    # RPC TLS
    rpc-ssl=autodetect             # Use TLS if client wallet supports it (Default); A new certificate will be regenerated every restart

    # ZMQ
    #zmq-rpc-bind-ip=127.0.0.1      # Default 127.0.0.1
    #zmq-rpc-bind-port=18082        # Default 18082
    zmq-pub=tcp://127.0.0.1:18083  # ZMQ pub
    #no-zmq=1                       # Disable ZMQ RPC server

    # Mempool size
    max-txpool-weight=2684354560   # Maximum unconfirmed transactions pool size in bytes (here ~2.5GB, default ~618MB)

    # Database sync mode
    #db-sync-mode=safe:sync	       # Slow but reliable db writes

    # Network limits
    out-peers=24              # This will enable much faster sync and tx awareness; the default 8 is suboptimal nowadays
    in-peers=48               # The default is unlimited; we prefer to put a cap on this

    limit-rate-up=1048576     # 1048576 kB/s == 1GB/s; a raise from default 2048 kB/s; contribute more to p2p network
    limit-rate-down=1048576   # 1048576 kB/s == 1GB/s; a raise from default 8192 kB/s; allow for faster initial sync

    # Tor/I2P: broadcast transactions originating from connected wallets over Tor/I2P (does not concern relayed transactions)
    tx-proxy=tor,127.0.0.1:9050,16,disable_noise  # Tor
    #tx-proxy=i2p,127.0.0.1:4447,16.disable_noise  # I2P

    # Tor/I2P: tell monerod your onion address so it can be advertised on P2P network
    anonymous-inbound=PASTE_YOUR_ONION_HOSTNAME:18084,127.0.0.1:18084,64
    #anonymous-inbound=PASTE_YOUR_I2P_HOSTNAME,127.0.0.1:18085,64

    # Tor: be forgiving to connecting wallets; suggested by http://xmrguide42y34onq.onion/remote_nodes
    disable-rpc-ban=1
    ```


    ### Systemd

7. Create `/etc/systemd/system/monerod.service` as shown below.

    ``` INI
    # /etc/systemd/system/monerod.service

    [Unit]
    Description=Monero Daemon
    After=network-online.target

    [Service]
    ExecStart=/usr/local/bin/monerod --detach --config-file /etc/monero/monerod.conf --pidfile /run/monero/monerod.pid
    ExecStartPost=/bin/sleep 0.1
    PIDFile=/run/monero/monerod.pid
    Type=forking

    Restart=on-failure
    RestartSec=30

    User=monero
    Group=monero
    RuntimeDirectory=monero

    StandardOutput=journal
    StandardError=journal

    [Install]
    WantedBy=multi-user.target
    ```

8. Enable the monerod service:

    ``` Bash
    systemctl daemon-reload
    systemctl enable monerod
    systemctl restart monerod
    ```

9. Verify it is up:

    ``` Bash
    systemctl status monerod
    ```

9. Verify it is working as intended:

    ``` Bash
    tail -n100 /var/log/monero/monero.log
    ```



## Open firewall ports

If you use a firewall (and you should), open `18080` and `18089` ports for incoming TCP connections.    
These are for the incoming **clearnet** connections, P2P and RPC respectively.

You **do not** need to open any ports for Tor.

For example, for popular ufw firewall, that would be:

``` Bash
ufw allow 18080/tcp
ufw allow 18089/tcp
```

To verify, use `ufw status`. The output should be similar to the following (the `22` being default SSH port, unrelated to Monero):

```
To                         Action      From
--                         ------      ----
22/tcp                     LIMIT       Anywhere
18080/tcp                  ALLOW       Anywhere
18089/tcp                  ALLOW       Anywhere
22/tcp (v6)                LIMIT       Anywhere (v6)
18080/tcp (v6)             ALLOW       Anywhere (v6)
18089/tcp (v6)             ALLOW       Anywhere (v6)
```


## Testing

### On server

List all services listening on ports and make sure it is what you expect:

``` Bash
sudo netstat -lntpu
```

The output should include these (in any order); obviously the PID values will differ.

```
Proto Recv-Q Send-Q Local Address           Foreign Address         State       PID/Program name
...
tcp        0      0 0.0.0.0:18080           0.0.0.0:*               LISTEN      259255/monerod
tcp        0      0 0.0.0.0:18089           0.0.0.0:*               LISTEN      259255/monerod
tcp        0      0 127.0.0.1:18084         0.0.0.0:*               LISTEN      259255/monerod
tcp        0      0 127.0.0.1:9050          0.0.0.0:*               LISTEN      258786/tor
```

### On client machine

Finally, we want to test connections from your client machine.

Install `tor` and `torsocks` on your laptop, you will want them anyway for Monero wallet.

Just for testing, you will also need `nmap` and `proxychains`.

Test **clearnet P2P** connection:

`nmap -Pn -p 18080 YOUR_IP_ADDRESS_HERE`

Test **clearnet RPC** connection:

`curl --digest -X POST http://YOUR_IP_ADDRESS_HERE:18089/json_rpc -d '{"jsonrpc":"2.0","id":"0","method":"get_info"}' -H 'Content-Type: application/json'`

Test **onion P2P** connection (skip if you don't have proxychains):

`proxychains nmap -Pn -p 18084 YOUR_ONION_ADDRESS_HERE.onion`

Test **onion RPC** connection:

`curl -x socks5h://127.0.0.1:9050 --digest -X POST http://YOUR_ONION_ADDRESS_HERE.onion:18089/json_rpc -d '{"jsonrpc":"2.0","id":"0","method":"get_info"}' -H 'Content-Type: application/json'`


## Debugging

Tor:

  * Status: `systemctl status tor@default`
  * Logs: `journalctl -xe --unit tor@default`

Monerod:

  * Status: `systemctl status monero`
  * Logs: `tail -n100 /var/log/monero/monero.log`
  * Logs more info: change `log-level=0` to `log-level=1` in `monero.conf` (remember to revert once solved)
