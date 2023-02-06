# Setup Stockfish Cluster
<h2>I. Getting ready</h2>
The Raspberry Pi 3 and higher is built with a 64-bit chip. Yet the Raspberry Pi Foundation has only released 32bit Linux distributions so far, but since March 2022 there is a 64-bullseye distribution. Replacing my existing Pi's with Le Potato I switched to Ubuntu server 64-bit images. Performance is way higher than with 32-bit images. However, recently I had a clash after Ubuntu update and switched to the very stable Armbian distribution for LePotato.
If you want to use Debian, start by downloading the latest version of Raspbian, the Debian distribution that runs on the Pis. Download the command-line only “lite” version to save space and create Image with raspberry PI Imager, Debian Lite. Before we finish with the SD card, we want to enable SSH remote access from our Pi. To do this, open the “boot” drive on the SD card and create an empty file named ssh with no extension. Create an empty via file with windows CMD with: copy nul “ssh” and voila, the file is created and named ssh (no extension) and copy to sd card.
Repeat with all SD cards for each node and don’t mix them up. Boot raspberry PI and login via SSH, user “pi”, password “raspberry” and run the updates. With Ubuntu or Armbian this is not necessary. Headless SBC installation is way easier.
The first installation will be our ClusterMaster.
After first login, update the system

```console
$ sudo apt-get update
$ apt-get upgrade -y
```
Setting up the ClusterMaster:
```console
$ hostnamectl set-hostname new-hostname
```
or
```console
$ sudo nano /etc/hostname and reboot
```
Additionally, I had to change the file /etc/cloud/cloud.cfg in the Ubuntu OS. There is a setting preserve_hostname: false and I had to change that from false to true.
Next step is to add a new user we want to use to run the Stockfish Cluster:
```console
$ adduser mpiuser
```
and add to sudoer group
```console
$ usermod -aG sudo mpiuser
```
It's easier to run sudo command without password. Therfore, login as newuser and get rid of password when entering sudo command with

```console
$ sudo bash -c 'echo "$(logname) ALL=(ALL:ALL) NOPASSWD: ALL" | (EDITOR="tee -a" visudo)'
```
Repeat this for all your nodes, name them such as CluserNode1-3, having this picture in mind.
<img src=".images/clusterarchitecture.jpeg" alt="Architecture" />
