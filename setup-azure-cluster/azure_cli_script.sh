#!/bin/bash
# Azure CLI commands 
# The script will create a resource group, a proximity placement group, 
# and VMs with a specified number of nodes

rg_name="myResourceGroup"
location="westus"
ppg_name="myclusterppg"
vm_name="mycluster"
image="UbuntuLTS"
size="Standard_DS1_v2"

read -p "Enter the number of nodes: " node_count

az group create --name $rg_name --location $location
az ppg create --name $ppg_name --resource-group $rg_name --instance-count $node_count --instance-size $size
for i in $(seq 1 $node_count); do
  az vm create --name "${vm_name}-${i}" --resource-group $rg_name --image $image --ppg $ppg_name --generate-ssh-keys --size $size --accelerated-networking true --custom-data cloud-init.txt
done
