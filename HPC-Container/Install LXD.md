Status of the SBC system:
## Docu installing LXD

```bash
sudo apt install snapd
```

``` bash
sudo snap install lxd
```
Add yourself to the LXD group 
```bash
sudo usermod -aG lxd pi
```

``` bash
snap list
Name    Version        Rev    Tracking       Publisher   Notes
core20  20230622       1977   latest/stable  canonical✓  base
lxd     5.0.2-838e1b2  24326  5.0/stable/…   canonical✓  -
snapd   2.60.4         20298  latest/stable  canonical✓  snapd
```

```bash
clush -w clusternode[1-3] -b
Enter 'quit' to leave this interactive mode
Working with nodes: clusternode[1-3]
clush> df -h
clush: 3/3
---------------
clusternode1
---------------
Filesystem      Size  Used Avail Use% Mounted on
tmpfs           194M  5.8M  188M   3% /run
/dev/mmcblk0p1   30G  2.4G   27G   9% /
tmpfs           966M     0  966M   0% /dev/shm
tmpfs           5.0M     0  5.0M   0% /run/lock
tmpfs           966M  8.0K  966M   1% /tmp
/dev/zram1       47M   22M   23M  49% /var/log
tmpfs           194M  4.0K  194M   1% /run/user/1000
---------------
clusternode2
---------------
Filesystem      Size  Used Avail Use% Mounted on
tmpfs           185M  3.1M  182M   2% /run
/dev/mmcblk0p2   30G  6.1G   22G  22% /
tmpfs           923M     0  923M   0% /dev/shm
tmpfs           5.0M     0  5.0M   0% /run/lock
/dev/mmcblk0p1  253M  143M  110M  57% /boot/firmware
tmpfs           185M  4.0K  185M   1% /run/user/1001
---------------
clusternode3
---------------
Filesystem      Size  Used Avail Use% Mounted on
tmpfs           194M  5.8M  188M   3% /run
/dev/mmcblk0p1   30G  2.8G   26G  10% /
tmpfs           966M     0  966M   0% /dev/shm
tmpfs           5.0M     0  5.0M   0% /run/lock
tmpfs           966M  4.0K  966M   1% /tmp
/dev/zram1       47M   20M   25M  45% /var/log
tmpfs           194M  4.0K  194M   1% /run/user/1000
clush> quit
```

### Initialize LXD on the master node
``` bash
ClusterMaster:~$ sudo lxd init
Would you like to use LXD clustering? (yes/no) [default=no]: yes
What IP address or DNS name should be used to reach this server? [default=10.0.0.175]:
Are you joining an existing cluster? (yes/no) [default=no]: n
What member name should be used to identify this server in the cluster? [default=ClusterMaster]:
Do you want to configure a new local storage pool? (yes/no) [default=yes]:
Name of the storage backend to use (btrfs, dir, lvm) [default=btrfs]:
Create a new BTRFS pool? (yes/no) [default=yes]:
Would you like to use an existing empty block device (e.g. a disk or partition)? (yes/no) [default=no]:
Size in GiB of the new loop device (1GiB minimum) [default=11GiB]:
Do you want to configure a new remote storage pool? (yes/no) [default=no]:
Would you like to connect to a MAAS server? (yes/no) [default=no]:
Would you like to configure LXD to use an existing bridge or host interface? (yes/no) [default=no]:
Would you like stale cached images to be updated automatically? (yes/no) [default=yes]:
Would you like a YAML "lxd init" preseed to be printed? (yes/no) [default=no]:
```

Which server are available?

``` bash 
lxc remote list
```

Output is

``` bash
To start your first container, try: lxc launch ubuntu:22.04
Or for a virtual machine: lxc launch ubuntu:22.04 --vm

+----------------------+---------------------------------------------------+---------------+-------------+--------+--------+--------+
|         NAME         |                        URL                        |   PROTOCOL    |  AUTH TYPE  | PUBLIC | STATIC | GLOBAL |
+----------------------+---------------------------------------------------+---------------+-------------+--------+--------+--------+
| images               | https://images.linuxcontainers.org                | simplestreams | none        | YES    | NO     | NO     |
+----------------------+---------------------------------------------------+---------------+-------------+--------+--------+--------+
| local (current)      | unix://                                           | lxd           | file access | NO     | YES    | NO     |
+----------------------+---------------------------------------------------+---------------+-------------+--------+--------+--------+
| ubuntu               | https://cloud-images.ubuntu.com/releases          | simplestreams | none        | YES    | YES    | NO     |
+----------------------+---------------------------------------------------+---------------+-------------+--------+--------+--------+
| ubuntu-daily         | https://cloud-images.ubuntu.com/daily             | simplestreams | none        | YES    | YES    | NO     |
+----------------------+---------------------------------------------------+---------------+-------------+--------+--------+--------+
| ubuntu-minimal       | https://cloud-images.ubuntu.com/minimal/releases/ | simplestreams | none        | YES    | YES    | NO     |
+----------------------+---------------------------------------------------+---------------+-------------+--------+--------+--------+
| ubuntu-minimal-daily | https://cloud-images.ubuntu.com/minimal/daily/    | simplestreams | none        | YES    | YES    | NO     |
+----------------------+---------------------------------------------------+---------------+-------------+--------+--------+--------+
```
adding a node with

``` bash
lxc cluster add clusternode1
Member clusternode1 join token:
here your token
```

``` bash
ClusterNode1:~$ sudo lxd init
Would you like to use LXD clustering? (yes/no) [default=no]: yes
What IP address or DNS name should be used to reach this server? [default=10.0.0.176]:
Are you joining an existing cluster? (yes/no) [default=no]: yes
Do you have a join token? (yes/no/[token]) [default=no]: yes
Please provide join token:
copy paste your token here

```

repeat for all nodes and ensure to have the same lxd version on the nodes. If not update with something like:

``` bash
sudo snap refresh lxd --channel=5.19/stable
```

``` bash
lxc cluster list
+---------------+-------------------------+------------------+--------------+----------------+-------------+--------+-------------------+
|     NAME      |           URL           |      ROLES       | ARCHITECTURE | FAILURE DOMAIN | DESCRIPTION | STATE  |      MESSAGE      |
+---------------+-------------------------+------------------+--------------+----------------+-------------+--------+-------------------+
| ClusterMaster | https://10.0.0.xxx:8443 | database-leader  | aarch64      | default        |             | ONLINE | Fully operational |
|               |                         | database         |              |                |             |        |                   |
+---------------+-------------------------+------------------+--------------+----------------+-------------+--------+-------------------+
| clusternode1  | https://10.0.0.xxx:8443 | database         | aarch64      | default        |             | ONLINE | Fully operational |
+---------------+-------------------------+------------------+--------------+----------------+-------------+--------+-------------------+
| clusternode2  | https://10.0.0.xxx:8443  | database-standby | aarch64      | default        |             | ONLINE | Fully operational |
+---------------+-------------------------+------------------+--------------+----------------+-------------+--------+-------------------+
| clusternode3  | https://10.0.0.xxx:8443   | database         | aarch64      | default        |             | ONLINE | Fully operational |
+---------------+-------------------------+------------------+--------------+----------------+-------------+--------+-------------------+
```

create a first container

``` bash
lxc launch images:ubuntu/focal
Creating the instance
Instance name is: better-lamprey

The instance you are starting doesn't have any network attached to it.
  To create a new network, use: lxc network create
  To attach a network to an instance, use: lxc network attach
```

``` bash
lxc network list
```
Creating the network on one node, you can add the other nodes. Here's how you can do it:

```bash
lxc network create lxdcluster
```

This will create the `lxdcluster` network across all nodes in the cluster as bridge.
``` bash
lxc network list
+------------+----------+---------+----------------+---------------------------+-------------+---------+---------+
|    NAME    |   TYPE   | MANAGED |      IPV4      |           IPV6            | DESCRIPTION | USED BY |  STATE  |
+------------+----------+---------+----------------+---------------------------+-------------+---------+---------+
| eth0       | physical | NO      |                |                           |             | 0       |         |
+------------+----------+---------+----------------+---------------------------+-------------+---------+---------+
| lxdcluster | bridge   | YES     | 10.145.23.1/24 | fd42:16df:e3c1:f2e6::1/64 |             | 0       | CREATED |
+------------+----------+---------+----------------+---------------------------+-------------+---------+---------+
```
You can add the other nodes clusternode1-3 to the lxdcluster network by making the network pending on each of these nodes.

``` bash
lxc network create lxdbr0 --target clusternode1
```

and do the same for the rest of the nodes.
Creating a first container

``` bash
lxc launch images:ubuntu/focal
Creating the instance
Instance name is: proud-boar

The instance you are starting doesn't have any network attached to it.
  To create a new network, use: lxc network create
  To attach a network to an instance, use: lxc network attach

lxc network attach lxdcluster proud-boar eth0
lxc list
+------------+---------+---------------------+-----------------------------------------------+-----------+-----------+---------------+
|    NAME    |  STATE  |        IPV4         |                     IPV6                      |   TYPE    | SNAPSHOTS |   LOCATION    |
+------------+---------+---------------------+-----------------------------------------------+-----------+-----------+---------------+
| proud-boar | RUNNING | 10.145.23.81 (eth0) | fd42:16df:e3c1:f2e6:216:3eff:feaf:7b81 (eth0) | CONTAINER | 0         | ClusterMaster |
+------------+---------+---------------------+-----------------------------------------------+-----------+-----------+---------------

lxc exec proud-boar -- /bin/bash
root@proud-boar:~#
```
``` bash
lxc network show lxdbr0
config:
  ipv4.address: 10.126.4.1/24
  ipv4.nat: "true"
  ipv6.address: fd42:4262:e27a:59d6::1/64
  ipv6.nat: "true"
description: ""
name: lxdbr0
type: bridge
used_by:
- /1.0/instances/co1
- /1.0/instances/co2
- /1.0/instances/co3
- /1.0/instances/co4
- /1.0/profiles/default
managed: true
status: Created
locations:
- ClusterMaster
- clusternode1
- clusternode2
- clusternode3
```
