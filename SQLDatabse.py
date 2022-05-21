from azure.mgmt.sql import SqlManagementClient
import Credentials

sql_client = SqlManagementClient(Credentials.credential, Credentials.subscription_id)

sql = sql_client.servers.list()
database = {}
SQL = {}
for data in sql:
    dict = {data}
    database[data.name] = dict
    SQL["Database"] = database

print(SQL)


