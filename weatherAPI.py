import requests 

def getWeather(apiKey, city):

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={apiKey}&units=imperial"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        
        temperature = data['main']['temp']
        weather_description = data['weather'][0]['description']

        return f"Temperature in {city}: {temperature}°F\nWeather: {weather_description}"
    else:
        return "Error fetching weather data. Please check city name and API key."

apiKey = "Go get your api key and put it here"
city = "San Diego"
print(getWeather(apiKey, city))




