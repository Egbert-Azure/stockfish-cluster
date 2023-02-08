#!/bin/bash
# Azure CLI Script removing public IP
rg_name="myResourceGroup"
vm_name_prefix="mycluster"
nic_name_prefix="myclusterVMNic"
public_ip_prefix="myclusterPublicIP"

for i in {1..3}; do
    nic_name="${nic_name_prefix}${i}"
    public_ip="${public_ip_prefix}${i}"
    az network nic ip-config update --resource-group $rg_name \
                                    --name "ipconfig${vm_name_prefix}${i}" \
                                    --nic-name $nic_name \
                                    --remove PublicIpAddress
    az network public-ip delete --resource-group $rg_name \
                                --name $public_ip
done
