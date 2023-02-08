# Setting up a Basic MPI Cluster in Azure

This guide outlines the simplest method for creating an MPI cluster in Azure. The steps provided here serve as a visual demonstration of the process and are not intended for use in a production High-Performance Computing (HPC) environment.

> **_NOTE:_** The cluster created will be able to run MPI across the general-purpose network in Azure. You need to ensure using the right subscription when executing commands in Azure CLI (`az account list` is listing your subscriptions, with `az account set --subscription "Your Azure Subscription"` you change the default subscription.

For training purposes, the guide will use cheaper virtual machines (Standard D2as v4 with 2 vcpus and 8 GiB memory or Standard DS1 v2 with 1 vcpu). However, for the final Stockfish chess engine cluster, it is recommended to use the Standard D8as v4 with 8 vcpus and 32 GiB memory or higher.

The cluster will use the standard Azure network private IP address instead of InfiniBand. All steps will be performed using the Azure CLI and it is assumed that you have already set it up with your Azure account and subscription.

Before you start ensure you have enough quota on Azure and ensure you have Azure CLI installed and activated in Powershell (or your preferred terminal). To execute commands you can easily run Azure CLI in Powershell and connect from your machine. Keep in mind that some commands will only work if you open cloud shell (such as cloud-init).
![Alt text](../images/Azure%20CLI%20local%20machine.png)
To use custom data, you must Base64-encode the contents before passing the data to the API--unless you're using a CLI tool that does the conversion for you, such as the Azure CLI. The size can't exceed 64 KB.

In the CLI, you can pass your custom data as a file, as the following example shows. The file will be converted to Base64.

The next step is to create a file in your current shell, named `cloud-init.txt`. Goal is to customize our VM nodes we want to create.
Here are the steps:

- Create a cloud-init configuration file: The cloud-init configuration file is a script that contains the customization that you want to apply to the virtual machine. The script should be written in YAML format.

- Pass the cloud-init configuration file to the virtual machine: You can pass the cloud-init configuration file to the virtual machine during creation or after creation by using the Azure CLI, Azure portal, or Azure Resource Manager templates.

- Start the virtual machine: Once the virtual machine has been created, start it, and cloud-init will apply the customizations specified in the configuration file.

For more information on cloud-init and examples of cloud-init configuration files, see the official cloud-init documentation: <https://cloud-init.io/>

To configure our MPI Cluster create the following `cloud-init.txt` in your Azure Cloud Shell including the following contents:

```
# cloud-config
package_upgrade: true
packages:
  - clustershell
  - openmpi-bin
  - libopenmpi-dev
  - python3-pip
  - python3-mpi4py
  - python3-numpy
```

This file will install the necessary packages (clustershell, openmpi-bin, and libopenmpi-dev) to run MPI on your cluster. Not mandatory, but maybe useful, installing mpi4py to run some python test scripts.

## Create a Resource Group

Create a resource group with the az group create command. An Azure resource group is a logical container into which Azure resources are deployed and managed. It is a way to group our cluster components and to keep them in the same network segment. Run the following command to create a resource group with your location (here westus):

```
az group create --name myResourceGroup --location westus
```

In case you made a mistake you can delete the group:

```
az group delete --name myResourceGroup
```

## Create a Proximity Placement Group

A proximity placement group (ppg) is used to keep all VMs within the same low-latency network. Run the following command to create a ppg with your choice of VM size:

```
az ppg create --name myclusterppg --resource-group myResourceGroup --intent-vm-sizes Standard_DS1_v2          
```

To delete the group:

```
az group delete --name myclusterppg
```

You can check if everything is ok with a simple az command:

``` consol
az ppg list -o table
Location    Name          ProximityPlacementGroupType    ResourceGroup
----------  ------------  -----------------------------  ---------------
westus      myclusterppg  Standard                       MYRESOURCEGROUP
```

## Create Compute Nodes

To create a group of four compute nodes in the ppg, run the following command:

```
az vm create --name mycluster --resource-group myResourceGroup --image UbuntuLTS --ppg myclusterppg --generate-ssh-keys --size Standard_DS1_v2 --accelerated-networking true --custom-data cloud-init.txt --count 4
```

This will create four VMs named mycluster0, mycluster1, mycluster2, and mycluster3. To see all the created resources, run:

``` consol
az resource list --resource-group myclusterstrg -o table
```

Now we check if everthing is up and running:

``` console
az resource list --resource-group myresourcegroup -o table
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
ssh-keygen -t rsa
cat ~/.ssh/id_rsa.pub
```

copy the key, and then login to `mycluster1-3'

``` console
cd .ssh
nano authorized_keys`
```

and paste the key in a new line, save the file.
You should now be able to connext to all nodes from `mycluster0`.
A first test with the famous `HelloWorld.c` (in MPI-Tests subfolder)

[Hello World Example](../MPI-Tests/HelloWorldTest/helloworld.c)

Copy to mycluster0 and compile with OpenMPI:

``` console
mpicc helloworld.c -o helloworld
```

The `helloworld` program has to be on mycluster 1-3 too. We can easily copy with

``` console
clush -w mycluster[1-3] -c helloworld
```

You can now execute:

``` console
mpirun --host mycluster0,mycluster1,mycluster2,mycluster3 ./helloworld

Hello world from processor mycluster0, rank 0 out of 4 processors
Hello world from processor mycluster3, rank 3 out of 4 processors
Hello world from processor mycluster1, rank 1 out of 4 processors
Hello world from processor mycluster2, rank 2 out of 4 processors
```

A first test with latency might be helpful.

# MPI Latency Test

is a benchmarking tool used to measure the latency (or response time) of a Message Passing Interface (MPI) communication between two MPI processes.

``` console
mpirun -np 2 --host cluster1,cluster2 ./osu-micro-benchmarks-6.1/install/libexec/osu-micro-benchmarks/mpi/pt2pt/osu_latency
```

The above example command uses the MPI implementation mpirun to launch two MPI processes on two separate hosts, cluster1 and cluster2. The benchmark is executed from the osu-micro-benchmarks-6.1 package and specifically the osu_latency test within the pt2pt MPI communication benchmark suite. The benchmark measures the time it takes for two MPI processes to send short messages to each other and can be used to evaluate the performance of MPI communication in a cluster computing environment.

### Installation:

``` console
wget https://mvapich.cse.ohio-state.edu/download/mvapich/osu-micro-benchmarks-6.1.tar.gz
tar zxf osu-micro-benchmarks-6.1.tar.gz
cd osu-micro-benchmarks-6.1/
./configure --prefix $PWD/install CC=mpicc CXX=mpicxx
make && make install
```

And then run a first test with:

 ``` console
 mpirun -np 2 mycluster1,mycluster2,mycluster3 ./osu-micro-benchmarks-6.1/install/libexec/osu-micro-benc
hmarks/mpi/pt2pt/osu_latency
```

To optimize an MPI cluster we can remove public IP addresses for all nodes but not the master.

``` vbnet
# Azure CLI Script

This script uses the Azure CLI to perform the following operations in a loop 3 times:

1. Remove a public IP address from a network interface configuration.
2. Delete a public IP.
```

``` bash
for i in {1..3}; do
    az network nic ip-config update --resource-group myResourceGroup \
                                    --name ipconfigmycluster${i} \
                                    --nic-name myclusterVMNic${i} \
                                    --remove PublicIpAddress
    az network public-ip delete --resource-group myResourceGroup \
                                --name myclusterPublicIP${i}
done
```

### Explanation:

This shell script updates the IP configuration of 3 network interfaces (`ipconfigmycluster1`, `ipconfigmycluster2`, `ipconfigmycluster3`) and removes their respective public IP addresses.
Then, it deletes 3 public IPs (`myclusterPublicIP1`, `myclusterPublicIP2`, `myclusterPublicIP3`) associated with these network interfaces.
All these resources belong to a resource group named `myResourceGroup`.
