# Setting up a Basic MPI Cluster in Azure
This guide outlines the simplest method for creating an MPI cluster in Azure. The steps provided here serve as a visual demonstration of the process and are not intended for use in a production High-Performance Computing (HPC) environment.

Note: The cluster created will be able to run MPI across the general-purpose network in Azure.

For training purposes, the guide will use cheaper virtual machines (Standard D2as v4 with 2 vcpus and 8 GiB memory or Standard DS1 v2 with 1 vcpu). However, for the final Stockfish chess engine cluster, it is recommended to use the Standard D8as v4 with 8 vcpus and 32 GiB memory or higher.

The cluster will use the standard Azure network private IP address instead of InfiniBand. All steps will be performed using the Azure CLI and it is assumed that you have already set it up with your Azure account and subscription.

To run the az commands, create a text `cloud-setup.txt` file in your PowerShell environment and include the following contents:
```
#cloud configuration
package_upgrade: true
packages:
  - clustershell
  - openmpi-bin
  - libopenmpi-dev
  - python3-pip
  - python3-mpi4py
```

This file will install the necessary packages (clustershell, openmpi-bin, and libopenmpi-dev) to run MPI on your cluster. Not mandatory, but maybe useful, installing mpi4py to run some python test scripts.
Before you start ensure you have enough quota on Azure.

<h2>Create a Resource Group</h2>
A resource group is a way to group our cluster components and to keep them in the same network segment. Run the following command to create a resource group with your location:

```
$ az group create --name mycluster --location westus
```
Create a Proximity Placement Group
A proximity placement group (ppg) is used to keep all VMs within the same low-latency network. Run the following command to create a ppg with your choice of VM size:

```
$ az ppg create --name myclusterppg --resource-group myclusterstrg --intent-vm-sizes Standard_DS1_v2          
```

<h2>Create Compute Nodes</h2>
To create a group of four compute nodes in the ppg, run the following command:

```
$ az vm create --name mycluster --resource-group myclusterstrg --image UbuntuLTS \
             --ppg myclusterppg --generate-ssh-keys --size Standard_DS1_v2 \
             --accelerated-networking true --custom-data cloud-setup.txt \
             --count 4
```
This will create four VMs named mycluster0, mycluster1, mycluster2, and mycluster3. To see all o see all the resources created, run:
``` consol
$ az resource list --resource-group myclusterstrg -o table
```

