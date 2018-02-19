"""
Present Weather Broadcaster
                     Michael
"""

import requests

api_address='http://api.openweathermap.org/data/2.5/weather?appid=0c42f7f6b53b244c78a418f4f181282a&q='
city = input('City Name :')
url = api_address + city
json_data = requests.get(url).json()

description = json_data['weather'][0]['main']
tempo = json_data['main']['temp']
humid = json_data['main']['humidity']

print('Climate: ')
print(description)

print('Temperature: ')
print(tempo)

print('Humidity: ')
print(humid)
