import requests
import json


r = requests.get('http://api.openweathermap.org/data/2.5/weather?q=London&APPID=df5f5fe0aa34488ff5a9930cea3b4d07')

output  = r.json()

# API KEY - df5f5fe0aa34488ff5a9930cea3b4d07

print output['name']
print output['weather'][0]['main']
print output['weather'][0]['description']







