# Azure Port Closing for Improved Network Security
Closing ports on a network can be a good practice for improving security and reducing the risk of security incidents. By limiting the number of open ports, you can reduce the attack surface of your network and make it more difficult for malicious actors to gain access to your resources.

Azure CLI script:
```
#!/bin/bash

# Define variables
RESOURCE_GROUP="myResourceGroup"
NSG_NAME="myclusterNSG"
VM_NICS=("mycluster0-nic" "mycluster1-nic" "mycluster2-nic" "mycluster3-nic")

# Remove all rules from the network security group
for nic in "${VM_NICS[@]}"; do
  RULES=$(az network nic show --resource-group $RESOURCE_GROUP --name $nic --query "networkSecurityGroup.id" --output tsv)
  if [ ! -z "$RULES" ]; then
    RULES=$(az network nsg rule list --ids $RULES --query "[].{Name: name}" --output tsv)
    for rule in $RULES; do
      echo "Removing rule: $rule"
      az network nsg rule delete --resource-group $RESOURCE_GROUP --nsg-name $NSG_NAME --name $rule
    done
  fi
done

# Create a new rule to allow SSH traffic
echo "Creating rule to allow SSH traffic"
az network nsg rule create --resource-group $RESOURCE_GROUP --nsg-name $NSG_NAME --name "allow-ssh" --priority 100 --destination-port-ranges 22 --access Allow

# List all rules in the network security group
echo "Listing all rules in the network security group"
az network nsg rule list --resource-group $RESOURCE_GROUP --nsg-name $NSG_NAME --output table
```
This script will first remove all existing rules from the network security group, then create a new rule to allow SSH traffic, and finally list all the rules in the network security group to verify that the new rule has been successfully implemented.
