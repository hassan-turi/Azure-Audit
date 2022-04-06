
"""Working code"""
import os
import Credentials
from azure.identity import AzureCliCredential
from azure.mgmt.resource import ResourceManagementClient

credential = AzureCliCredential()

resource_client = ResourceManagementClient(credential, Credentials.subscription_id)
group_list = resource_client.resource_groups.list()
lst = []
dict_Resource_Group = {}
for group in group_list:
    lst.append(group.name)
    # print(group.as_dict())
    dict = {"Group_Name": group.name,"Group_Location":group.location}
    dict_Resource_Group["Resorce_Group"] = (dict)
# dict_Resource_Group.update(lst)
demo = lst[1]
other = lst[0]
# print("Resource Group Names",dict_Resource_Group)

"""subscription_id = os.environ["8abf0e0e-3787-4d52-92a1-98258b7561cb"]
tenant_id = os.environ['75df096c-8b72-48e4-9b91-cbf79d87ee3a']
client_id = os.environ['6ba20ca0-9eac-47df-a48a-69a935cf3841']
client_secret = os.environ['Kqh7Q~gxKhu52LTHbJyGiWGEBRff2Zcfw3O3K']"""
