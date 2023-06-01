from azure.common.credentials import ServicePrincipalCredentials
from azure.identity import ClientSecretCredential

credential = ServicePrincipalCredentials(client_id='XXXXXX',
                                         secret='WtM8Q~XXXXXX', tenant='XXXXXX')

subscription_id = "XXXXXX"


acredential = ClientSecretCredential(client_id='XXXXXX',
                                         client_secret='XXXXXX', tenant_id='XXXXXX')
