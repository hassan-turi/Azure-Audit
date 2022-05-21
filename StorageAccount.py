import Credentials
from azure.mgmt.storage import StorageManagementClient
from pprint import pprint


storage_client = StorageManagementClient(Credentials.acredential,Credentials.subscription_id)

skus = {sku.name for sku in storage_client.skus.list()}

dict = {e:"Storage_Account" for e in skus}

storage = {"Storge_Accounts": dict}

# pprint(storage)




# for sku in storage_client.skus.list():

#     print(sku.name)