# Written by User9684
import json
import requests
from prettytable import PrettyTable

req = requests.get('https://api.statusplus.xyz/status')
statuses = req.json()
newTable = PrettyTable()
newTable.field_names = ['API Name','Status','Response Time (ms)','HTTP Code']

for api in statuses:
    newTable.add_row([api['name'],api['status'],api['response_time'],api['response_code']])

print(newTable)