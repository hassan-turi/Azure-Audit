from azure.mgmt.keyvault import KeyVaultManagementClient
import Credentials
from pprint import pprint
import ResourceGoup

client = KeyVaultManagementClient(Credentials.credential, Credentials.subscription_id)
mapping = {}
KeyVault = {}
for group in ResourceGoup.ResourceName:
    # print(group)
    vaults = client.vaults.list_by_resource_group(group)  # replace with your resource group name
    
    for vault in vaults:
        # pprint(vault.as_dict())
        
        dict = {"Name":vault.name, "Location": vault.location,"Purge_Protection":vault.properties.enable_purge_protection,"disk_encryption":vault.properties.enabled_for_disk_encryption,"Vault_uri":vault.properties.vault_uri}
        mapping[vault.name] = dict
        KeyVault["Key_Vaults"] = mapping

# pprint(KeyVault)



    # print("Vault found: {}".format(vault.name))
    # mapping[vault.name] = []

#     access_policies = vault.properties.access_policies
#     for access_policy in access_policies:
#         print("Object ID of principal: {}".format(access_policy.object_id))
#         print("Permissions: {}".format(access_policy.permissions))
#         mapping[vault.name].append((access_policy.object_id, access_policy.permissions))

# print(mapping)