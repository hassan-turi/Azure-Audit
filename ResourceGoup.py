import Credentials
from azure.mgmt.resource import ResourceManagementClient
from pprint import pprint

credential = Credentials.credential

resource_client = ResourceManagementClient(credential, Credentials.subscription_id)
group_list = resource_client.resource_groups.list()

dict_Resource_Group = {}
Resource_dict = {}
ResourceName = []
for group in group_list:
    dict = {"Group_Name": group.name,"Group_Location":group.location}
    dict_Resource_Group[group.name] = (dict)

    ResourceName.append(group.name)

    Resource_dict["Resources_Groups"] = dict_Resource_Group

# print(Resource_dict)
# print(ResourceName)

