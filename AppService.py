from azure.common.credentials import ServicePrincipalCredentials
from azure.mgmt.resource import ResourceManagementClient
from azure.mgmt.web import WebSiteManagementClient
import Credentials


web_client = WebSiteManagementClient(Credentials.credential, Credentials.subscription_id)

for site in web_client.web_apps.list():
    print("hello",site)
    