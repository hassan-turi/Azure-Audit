from azure.mgmt.security import SecurityCenter
import Credentials
from pprint import pprint

scoreDict = {}
SecurityGroup = {}
client = SecurityCenter(Credentials.acredential,Credentials.subscription_id,asc_location="")
for score in client.secure_scores.list():
    dict = {"Security_Name":score.name, "Max_Score":score.max,"Current_Score":score.current}
    scoreDict[score.name] = dict
    SecurityGroup["Security_Center"] = scoreDict

# pprint(SecurityGroup)