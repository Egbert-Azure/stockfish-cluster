#!/bin/bash
# Azure Cluster Port Closing for Improved Network Security
# Replace these values with your own

RESOURCE_GROUP="myResourceGroup"
NSG_NAME="myclusterNSG"
VM_NICS=("mycluster0-nic" "mycluster1-nic" "mycluster2-nic" "mycluster3-nic")

# Create the NSG rule to allow only SSH traffic
az network nsg rule create \
  --resource-group $RESOURCE_GROUP \
  --nsg-name $NSG_NAME \
  --name Allow-SSH \
  --priority 100 \
  --destination-port-ranges 22 \
  --protocol tcp \
  --access allow

# Associate the NSG with each of the VMs
for nic in "${VM_NICS[@]}"; do
  az network nic update \
    --resource-group $RESOURCE_GROUP \
    --name $nic \
    --network-security-group $NSG_NAME
done
