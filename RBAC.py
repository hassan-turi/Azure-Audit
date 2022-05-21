from azure.common.credentials import ServicePrincipalCredentials
from azure.mgmt.authorization import AuthorizationManagementClient
import Credentials
from pprint import pprint


RBAC_dict = {}
RBAC = {}
client = AuthorizationManagementClient(Credentials.credential, Credentials.subscription_id)
roles = client.role_assignments.list()
for role in roles:
    # pprint(role.as_dict())
    dict = {"Name":role.name,  "Type":role.type}
    RBAC_dict[role.name] = dict
    RBAC["Role_Base_Access_Control"] = RBAC_dict

# pprint(RBAC)
