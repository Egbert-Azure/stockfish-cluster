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
