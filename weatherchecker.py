import requests

api_key =
city = input('Enter your city: ')
url = "http://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=" + api_key + '&units=metric'

res = requests.get(url)

data = res.json()

temp = data['main']['temp']
weather = data['weather'][0]['main']

print("The temperature is: {} degree celcius".format(temp))
print("The weather is: {}!".format(weather))