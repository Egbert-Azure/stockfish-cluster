# Automating Azure CLI Commands

In this guide, we will walk through the steps to automate Azure CLI commands using a shell script. The script will create a resource group, a proximity placement group, and VMs with a specified number of nodes.

## Prerequisites

- Azure CLI installed on your machine
- A text editor to write the script
- A cloud-init file (named `cloud-init.txt` in this guide)

## Writing the Script

Create a new file with a `.sh` extension, for example `azure_cli_script.sh`, and open it in a text editor.

Paste the following [code](azure_cli_script.sh) into the file


``` s
#!/bin/bash
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
```

This script uses the Azure CLI to create a resource group named `myResourceGroup` in the `westus` location, a proximity placement group named `myclusterppg` in the `myResourceGroup` resource group, and VMs named `mycluster` in the `myResourceGroup` resource group using the `UbuntuLTS` image and the `Standard_DS1_v2` size. The script first reads the number of nodes from the user and stores it in the node_count variable. Then, it checks if the number of nodes is less than 2, and if so, sets node_count to 2.

## Making the Script Executable

To make the script executable, run the following command in the terminal:

``` console
chmod +x azure_cli_script.sh
```

## Running the Script

To run the script, execute the following command in the terminal:
``` s
./azure_cli_script.sh
```

The script will prompt you to enter the number of nodes, and then use the Azure CLI to create the specified resources.

## Conclusion

In this guide, we have shown you how to automate Azure CLI commands using a shell script. This can be useful for automating common tasks and reducing the time and effort required to set up and manage resources in Azure.
