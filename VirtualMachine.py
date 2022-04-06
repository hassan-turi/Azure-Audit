from azure.common.credentials import ServicePrincipalCredentials
from azure.mgmt.compute import ComputeManagementClient
import Credentials
import json

# credential = ServicePrincipalCredentials(client_id='6ba20ca0-9eac-47df-a48a-69a935cf3841',
#                                          secret='Kqh7Q~gxKhu52LTHbJyGiWGEBRff2Zcfw3O3K', tenant='75df096c-8b72-48e4-9b91-cbf79d87ee3a')
compute_client = ComputeManagementClient(
    Credentials.credential, Credentials.subscription_id)

#  source Azure/Scripts/activate


dict_VM = {}
for vm in compute_client.virtual_machines.list_all():
    # print(vm.hardware_profile.vm_size)
    # print("Virtual_Machines: ",vm.as_dict())
    # print(vm.storage_profile.os_disk.name)
    # print(vm.storage_profile.os_disk.encryption_settings)
    # print(vm.storage_profile.os_disk.managed_disk.storage_account_type)
    # print(vm.storage_profile.image_reference.as_dict())
    new_dict = {"VM_Name": vm.name, "VM_Location":vm.location,  "VM_Disk_Name":vm.storage_profile.os_disk.name, "VM_Publisher_Info":vm.storage_profile.image_reference.as_dict(), "Vm_Disk_Type":vm.hardware_profile.vm_size , "VM_Encryption":vm.storage_profile.os_disk.encryption_settings}
    dict_VM['Virtual_Machine'] = (new_dict)
# print("Virtual Machines Details",dict_VM)