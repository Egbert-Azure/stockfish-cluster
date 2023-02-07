# Setting up a Basic MPI Cluster in Azure
This guide outlines the simplest method for creating an MPI cluster in Azure. The steps provided here serve as a visual demonstration of the process and are not intended for use in a production High-Performance Computing (HPC) environment.

Note: The cluster created will be able to run MPI across the general-purpose network in Azure.

For training purposes, the guide will use cheaper virtual machines (Standard D2as v4 with 2 vcpus and 8 GiB memory or Standard DS1 v2 with 1 vcpu). However, for the final Stockfish chess engine cluster, it is recommended to use the Standard D8as v4 with 8 vcpus and 32 GiB memory or higher.

The cluster will use the standard Azure network private IP address instead of InfiniBand. All steps will be performed using the Azure CLI and it is assumed that you have already set it up with your Azure account and subscription.

Before you start ensure you have enough quota on Azure and ensure you have Azure CLI installed and activated in Powershell (or your preferred terminal). To execute commands you can easily run Azure CLI in Powershell and connect from your machine. Keep in mind that some commands will only work if you open cloud shell (such as cloud-init).

To use custom data, you must Base64-encode the contents before passing the data to the API--unless you're using a CLI tool that does the conversion for you, such as the Azure CLI. The size can't exceed 64 KB.

In the CLI, you can pass your custom data as a file, as the following example shows. The file will be converted to Base64.

The next step is to create a file in your current shell, named `cloud-init.txt` in your PowerShell environment and include the following contents:
```
# cloud-config
package_upgrade: true
packages:
  - clustershell
  - openmpi-bin
  - libopenmpi-dev
  - python3-pip
  - python3-mpi4py
```

This file will install the necessary packages (clustershell, openmpi-bin, and libopenmpi-dev) to run MPI on your cluster. Not mandatory, but maybe useful, installing mpi4py to run some python test scripts.


<h2>Create a Resource Group</h2>
Create a resource group with the az group create command. An Azure resource group is a logical container into which Azure resources are deployed and managed. It is a way to group our cluster components and to keep them in the same network segment. Run the following command to create a resource group with your location (here westus):

```
$ az group create --name myResourceGroup --location westus
```
In case you made a mistake you can delete the group:
```
$ az group delete --name myResourceGroup
```
<h2>Create a Proximity Placement Group</h2>
A proximity placement group (ppg) is used to keep all VMs within the same low-latency network. Run the following command to create a ppg with your choice of VM size:

```
$ az ppg create --name myclusterppg --resource-group myResourceGroup --intent-vm-sizes Standard_DS1_v2          
```
To delete the group:
```
$ az group delete --name myclusterppg
```
You can check if everything is ok with a simple az command:
``` consol
az ppg list -o table
Location    Name          ProximityPlacementGroupType    ResourceGroup
----------  ------------  -----------------------------  ---------------
westus      myclusterppg  Standard                       MYRESOURCEGROUP
```

<h2>Create Compute Nodes</h2>
To create a group of four compute nodes in the ppg, run the following command:

```
$ az vm create --name mycluster --resource-group myResourceGroup --image UbuntuLTS --ppg myclusterppg --generate-ssh-keys --size Standard_DS1_v2 --accelerated-networking true --custom-data cloud-init.txt --count 4
```
This will create four VMs named mycluster0, mycluster1, mycluster2, and mycluster3. To see all o see all the resources created, run:
``` consol
$ az resource list --resource-group myclusterstrg -o table
```
Now we check if everthing is up and running:
``` console
$ az resource list --resource-group myresourcegroup -o table
```
The compute nodes that are created have public IP addresses and are located in a shared subnet on the same Virtual Network (VNet), with close physical proximity, due to the proximity placement group (ppg). To view the IP addresses, you can run the following command:
```css
$ az vm list-ip-addresses --resource-group myresourcegroup -o table

VirtualMachine    PublicIPAddresses    PrivateIPAddresses
----------------  -------------------  --------------------
mycluster0        X.X.X.1               Y.Y.Y.5
mycluster1        X.X.X.56              Y.Y.Y.4 
```
Replace X.X.X.1 and X.X.X.56 with the actual public IP addresses of your compute nodes and Y.Y.Y.5 and Y.Y.Y.4 with their respective private IP addresses

The `az vm create` command created a user on each of the VMs with the same name as the local user who ran the command (e.g. mpiuser), but this can be overridden using `--admin-username` `yourusername` (mpiuser e.g.) in the command line. Additionally, the local SSH key (~/.ssh/id_rsa.pub) was added to each VM's authorized_keys file. As a result, you should now be able to log into your head node via PowerShell with `ssh mpiuser@PublicIPAddress`.

To start working with our new cluster we need to ssh from mycluster0 to mycluster 1-4. I do not recommend for security reason to use your local machine public key. A better way is to create a key on `mycluster0` and copy the key to `mycluster1-3`.

Create ssh key on `mycluster0`:
``` console
$ ssh-keygen -t rsa
$ cat ~/.ssh/id_rsa.pub
```
copy the key, and then login to `mycluster1-3' 
``` console 
$ cd .ssh
$ nano authorized_keys`
```
and paste the key in a new line, save the file.
You should now be able to connext to all nodes from `mycluster0`.


