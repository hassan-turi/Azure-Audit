from azure.common.credentials import ServicePrincipalCredentials
from azure.identity import ClientSecretCredential

credential = ServicePrincipalCredentials(client_id='ef13c065-188e-4f54-87d1-d15f2b046130',
                                         secret='WtM8Q~uM0erSC7kUhhvGwFVpZUSokSXdxrgXbda4', tenant='75df096c-8b72-48e4-9b91-cbf79d87ee3a')

subscription_id = "0837638e-463c-483c-a424-07651b04c67a"


acredential = ClientSecretCredential(client_id='ef13c065-188e-4f54-87d1-d15f2b046130',
                                         client_secret='WtM8Q~uM0erSC7kUhhvGwFVpZUSokSXdxrgXbda4', tenant_id='75df096c-8b72-48e4-9b91-cbf79d87ee3a')