#!/bin/bash
# Azure CLI commands using a shell script
# The script will create a resource group, a proximity placement group, 
# and VMs with a specified number of nodes

rg_name="myResourceGroup"
location="westus"
ppg_name="myclusterppg"
vm_name="mycluster"
image="UbuntuLTS"
size="Standard_DS1_v2"

echo "Enter the number of nodes:"
read node_count

az group create --name $rg_name --location $location
az ppg create --name $ppg_name --resource-group $rg_name --intent-vm-sizes $size
az vm create --name $vm_name --resource-group $rg_name --image $image --ppg $ppg_name --generate-ssh-keys --size $size --accelerated-networking true --custom-data cloud-init.txt --count $node_count
