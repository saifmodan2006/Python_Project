import requests,json

api_key = "Add Api Key"

base_url = "http://api.openweathermap.org/data/2.5/weather"

city_name = input("Enter city name:")

complete_url = base_url + "appid=" + api_key + "&q" + city_name

response = requests.get(complete_url)

x = response.json()

if x["cloud"] != "404":
    y = x['main']

    current_tempreature = y['temp']

    current_pressure = y['pressure']

    current_humidity = y['humidity']
    