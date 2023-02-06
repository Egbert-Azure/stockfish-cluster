# Setting up a Basic MPI Cluster in Azure
This guide outlines the simplest method for creating an MPI cluster in Azure. The steps provided here serve as a visual demonstration of the process and are not intended for use in a production High-Performance Computing (HPC) environment.

Note: The cluster created will be able to run MPI across the general-purpose network in Azure.

For training purposes, the guide will use cheaper virtual machines (Standard D2as v4 with 2 vcpus and 8 GiB memory). However, for the final STockfish chess engine cluster, it is recommended to use the Standard D8as v4 with 8 vcpus and 32 GiB memory or higher.

The cluster will use the standard Azure network private IP address instead of InfiniBand. All steps will be performed using the Azure CLI and it is assumed that you have already set it up with your Azure account and subscription.

To run the az commands, create a text file in your PowerShell environment and include the following contents:
```yaml 
#cloud configuration
package_upgrade: true
packages:
  - clustershell
  - openmpi-bin
  - libopenmpi-dev
```

This file will install the necessary packages (clustershell, openmpi-bin, and libopenmpi-dev) to run MPI on your cluster.
Before you start ensure you have enough quota on Azure.
