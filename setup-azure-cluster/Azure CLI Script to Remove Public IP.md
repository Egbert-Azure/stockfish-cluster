## Azure CLI Script to Remove Public IP
This script removes the public IP addresses from the specified network interface configurations and deletes the public IP addresses in a resource group.

## Variables
The following variables are defined at the beginning of the script:

```
rg_name: The name of the resource group.
vm_name_prefix: The prefix of the virtual machine name.
nic_name_prefix: The prefix of the network interface name.
public_ip_prefix: The prefix of the public IP address name.
```
### Usage
Make sure you have the Azure CLI installed and logged in to your Azure account.
Save the script to a file with a .sh extension, for example remove_public_ip.sh.
Run the script by executing bash remove_public_ip.sh in a terminal window.
### Script Details
The script uses a for loop to update the IP configuration of network interfaces and delete the corresponding public IP addresses. The loop runs three times, based on the value of i. The values of nic_name and public_ip are generated based on the prefixes and the current value of i. The az network nic ip-config update and az network public-ip delete commands are then used to remove the public IP addresses.