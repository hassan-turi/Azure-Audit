from azure.common.credentials import ServicePrincipalCredentials
from azure.mgmt.compute import ComputeManagementClient
import Credentials
import json
from pprint import pprint


compute_client = ComputeManagementClient(
    Credentials.credential, Credentials.subscription_id)

#  source Azure/Scripts/activate


dict_VM = {}
virtualMachine = {}
for vm in compute_client.virtual_machines.list_all():
    # print(vm.hardware_profile.vm_size)
    # print("Virtual_Machines: ",vm.as_dict())
    # print(vm.storage_profile.os_disk.name)
    # print(vm.storage_profile.os_disk.encryption_settings)
    # print(vm.storage_profile.os_disk.managed_disk.storage_account_type)
    # print(vm.storage_profile.image_reference.as_dict())
    new_dict = {"VM_Name": vm.name, "VM_Location":vm.location,  "VM_Disk_Name":vm.storage_profile.os_disk.name, "VM_Publisher_Info":vm.storage_profile.image_reference.as_dict(), "Vm_Disk_Type":vm.hardware_profile.vm_size , "VM_Encryption":vm.storage_profile.os_disk.encryption_settings}
    dict_VM[vm.name] = (new_dict)
    virtualMachine["Virtual_Machines"] = dict_VM
# pprint(virtualMachine)

"""
To loop over machines
"""

# for vm in dict_VM:
#     # print(f"======Virtual Machine: {vm}=======\nDetails: ", end="")
#     pprint(dict_VM[vm])
#     print()
