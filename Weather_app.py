import requests
api_key = '3e2dbc031eb13224ccc14992d8db787c'
city = input('Enter city name: ')
url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    temp = data['main']['temp']
    feels_like = data['main']['feels_like']
    hum = data['main']['humidity']
    pressure = data['main']['pressure']
    desc = data['weather'][0]['description']
    print(f'Temperature (kelvin): {temp} K')
    print(f'Tempearture (Celcius): {temp-273.15}')
    print(f'Description: {desc}')
    print(f'Feels Like: {feels_like}')
    print(f'Humidity: {hum}')
    print(f'Air Pressure: {pressure}')
else:
    print('Error fetching weather data')
