import requests

def get_weather(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'
    }
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return None

if __name__ == "__main__":
    api_key = "31e3234bfd0a6c9641d80bc850e9fcd0"
    city = "London"
    weather_data = get_weather(api_key, city)
    if weather_data:
        print(f"Weather in {city}: {weather_data['weather'][0]['description']}")
        print(f"Temperature: {weather_data['main']['temp']}°C")
    else:
        print("Failed to fetch weather data")