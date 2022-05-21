from azure.mgmt.network import NetworkManagementClient
import ResourceGoup
import Credentials
from pprint import pprint


credential = Credentials.credential

network_client = NetworkManagementClient(credential, Credentials.subscription_id)

dict_VN = {}
VirtualNetwork ={}
for net in ResourceGoup.ResourceName:
    network = network_client.virtual_networks.list(net)
    for vn in network:
        # print("Virtual_Networks: ",vn.as_dict())
        dict = {"Network_Name": vn.name,"Network_Type":vn.type , "Location": vn.location, "DDOS_Protection": vn.enable_ddos_protection, "VM_Protection":vn.enable_vm_protection, "DDOS_Protection_Plan":vn.ddos_protection_plan}
        dict_VN[vn.name] = (dict)
        VirtualNetwork["Virtual_Networks"] = dict_VN
# pprint(VirtualNetwork)

# network = network_client.virtual_networks.list(ResourceGoup.other)
# for vn in network:
#     print("Virtual_Networks: ",vn.as_dict())