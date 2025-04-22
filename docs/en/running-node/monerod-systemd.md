---
title: Running a Monero Node via Systemd

config: (#monerod-config)

configfile: "/etc/monero/monerod.conf"
datadir: "/var/lib/monero/bitmonero"
logfile: "log-file=/var/log/monero/monero.log"
maxlogsize: "max-log-file-size=2147483648   # Set to 2GB to mitigate log trimming by monerod; configure logrotate instead"
txproxyi2p:
txproxytor:
publicnode: "#public-node=1                  # Advertise to other users they can use this node for connecting their wallets"

---
# Running Monerod via Systemd
!!! success "The end goal"
    You will publicly offer the following services, where xxx.yyy.zzz.vvv is your server IP address.

    * xxx.yyy.zzz.vvv:18080 - clearnet P2P service (for other nodes)
    * xxx.yyy.zzz.vvv:18089 - clearnet RPC service (for wallets)

## Why run this specific setup?

You will be able to connect your desktop and mobile Monero wallets to your own trusted Monero node,
in a secure and private way over Tor.

**Running as a systemd service** will allow your node to always remain synced, as opposed to intermittently running node.

**Public RPC service** - The `public-node` config option will broadcast your RPC port to your peers, providing a service for anyone to use your node to connect their wallets to the Monero network.
This is useful to users who don't run their own nodes. You may enable it by removing the `#` from `#public-node` in the config.

??? warning "Public RPC may be resource intensive"
    Providing Public RPC via the flag `public-node=1` may use a sizeable amount of resources on your PC.

## Assumptions

You possess:

- Basic understanding of Linux administration
- Root access to a Linux server
- _Recommended_ 4 GB+ RAM
- _Recommended_ available SSD storage of
    - **{{ multiply(lmdb_size_full, 2.5) }} GB+** for the full node
    - **{{ multiply(lmdb_size_pruned, 2.5) }} GB+** for the pruned

!!! note "Current blockchain size as of {{ lmdb_size_updated }}"
    The current blockchain sizes are approximately:    
    Full node: **{{ lmdb_size_full }} GB**    
    Pruned node: **{{ lmdb_size_pruned }} GB**

Some commands assume Ubuntu but you will easily translate them to your distribution.

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

### Monerod Config

6. Create `/etc/monero/monerod.conf` as shown below:

{% include 'monerod_template' %}

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



### Open firewall ports

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

## Tor & I2P
??? tip "Tor Setup"
{% include 'tor_template' %}

??? tip "I2P Setup"
{% include 'i2pd_template' %}

### Testing

??? "Testing"

    **On server**

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

    **On client machine**

    Finally, we want to test connections from your client machine.

    Install `tor` and `torsocks` on your laptop, you will want them anyway for Monero wallet.

    Just for testing, you will also need `proxychains`.

    Test **clearnet P2P** connection:

    `nc -zv YOUR_IP_ADDRESS_HERE 18080`

    Test **clearnet RPC** connection:

    ``` Bash
    curl --digest -X POST http://YOUR_IP_ADDRESS_HERE:18089/json_rpc -d '{"jsonrpc":"2.0","id":"0","method":"get_info"}' -H 'Content-Type: application/json'
    ```

    Test **onion P2P** connection (skip if you don't have proxychains):

    ``` Bash
    proxychains nc -zv YOUR_IP_ADDRESS_HERE 18084
    ```

    Test **onion RPC** connection:

    ``` Bash
    curl -x socks5h://127.0.0.1:9050 --digest -X POST http://YOUR_ONION_ADDRESS_HERE.onion:18089/json_rpc -d '{"jsonrpc":"2.0","id":"0","method":"get_info"}' -H 'Content-Type: application/json'
    ```

### Debugging
??? Debugging
    Tor:

    - Status: `systemctl status tor@default`
    - Logs: `journalctl -xe --unit tor@default`

    Monerod:

    - Status: `systemctl status monero`
    - Logs: `tail -n100 /var/log/monero/monero.log`
    - Logs more info: change `log-level=0` to `log-level=1` in `monero.conf` (remember to revert once solved)
