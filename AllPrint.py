from operator import ne
import VirtualMachine
import ResourceGoup
import Networks
import json

vm = VirtualMachine.dict_VM
rg = ResourceGoup.dict_Resource_Group
network = Networks.dict_VN



with open('Audit.json', 'w') as file:
    json.dump((vm,rg,network),file,ensure_ascii=False,indent=6)