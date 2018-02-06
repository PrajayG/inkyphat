import requests
import json


r = requests.get('http://api.openweathermap.org/data/2.5/weather?q=London&APPID=df5f5fe0aa34488ff5a9930cea3b4d07&units=metric')
output  = r.json()

# API KEY - df5f5fe0aa34488ff5a9930cea3b4d07

print output['name']
print output['weather'][0]['main']
print output['weather'][0]['description']
print output['main']['temp_min']
weather = 'Today in London, the weather should be ' + output['weather'][0]['main'] + ' - ' + output['weather'][0]['description'] + 'There is a minimum temparature of' + output['main']['temp_min'] + ' and a max temperature of ' +  output['main']['temp_min']


print weather

