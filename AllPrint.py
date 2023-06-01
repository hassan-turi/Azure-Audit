import VirtualMachine
import ResourceGoup
import Networks
import RBAC
import KeyVaults
import SecurityGroups
import StorageAccount
from pymongo import MongoClient
import json


vm = VirtualMachine.virtualMachine
rg = ResourceGoup.Resource_dict
network = Networks.VirtualNetwork
rbac = RBAC.RBAC
kv = KeyVaults.KeyVault
sg = SecurityGroups.SecurityGroup
sa = StorageAccount.storage


client = MongoClient("MongoDB stirng")
db = client['Audit']
vms = db['virtual_machine']

# vm = json.dumps(vm)

vms = db['Report']


with open('Audit.json', 'w') as file:
    json.dump((vm,rg,network,rbac,kv,sg,sa),file,ensure_ascii=False,indent=5)


# vmachine = vms.find_one({"Virtual_Machines"},{'_id':0})    
# print(vmachine)

# vms.insert_one(vm)

with open("Audit.json",'rb') as file:
    data = json.load(file)
    # print(type(data))
    # print(data)
    
    vms.insert_many(data)
    
client.close()
