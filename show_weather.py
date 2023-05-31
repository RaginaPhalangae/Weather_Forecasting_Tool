import datetime as dt
import requests
import sys

BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"

def kelvin_to_celsius_to_fahrenheit(kelvin):
    celsius = kelvin - 273.15
    fahrenheit = celsius * (9/5) + 32
    return celsius, fahrenheit

def get_weather(city):
    API_KEY=input("Enter API Key for Open Weather Map Api : ")
    params = {
        "appid": API_KEY,
        "q": city
    }

    try:
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()  # Raise an exception for non-successful status codes

        data = response.json()
        
        main_data = data.get('main', {})
        weather_data = data.get('weather', [{}])[0]
        sys_data = data.get('sys', {})

        temp_kelvin = main_data.get('temp')
        feels_like_kelvin = main_data.get('feels_like')
        wind_speed = data.get('wind', {}).get('speed')
        humidity = main_data.get('humidity')
        description = weather_data.get('description')
        sunrise_time = dt.datetime.utcfromtimestamp(sys_data.get('sunrise', 0) + data.get('timezone', 0))
        sunset_time = dt.datetime.utcfromtimestamp(sys_data.get('sunset', 0) + data.get('timezone', 0))

        if temp_kelvin is not None and feels_like_kelvin is not None:
            temp_celsius, temp_fahrenheit = kelvin_to_celsius_to_fahrenheit(temp_kelvin)
            feels_like_celsius, feels_like_fahrenheit = kelvin_to_celsius_to_fahrenheit(feels_like_kelvin)

            print(f"Temperature in {city}: {temp_celsius:.2f}°C or {temp_fahrenheit:.2f}°F")
            print(f"Temperature in {city} feels like: {feels_like_celsius:.2f}°C or {feels_like_fahrenheit:.2f}°F")
            print(f"Humidity in {city}: {humidity}%")
            print(f"Wind Speed in {city}: {wind_speed}m/s")
            print(f"General Weather in {city}: {description}")
            print(f"Sun rises in {city}: {sunrise_time} local time")
            print(f"Sun sets in {city}: {sunset_time} local time")
        else:
            print("Failed to retrieve weather information.")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while making the request: {e}")
    except (KeyError, IndexError) as e:
        print(f"Error occurred while parsing weather data: {e}")
    except ValueError as e:
        print(f"Error occurred while decoding JSON response: {e}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        city_name = ' '.join(sys.argv[1:])
        get_weather(city_name)
    else:
        print("Please provide a city name as a command-line argument.")
