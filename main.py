import os
import requests
from dotenv import load_dotenv

def get_weather(api_key, location, units='metric'):
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    params = {
        'appid': api_key,
        'q': location,
        'units': units
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.ConnectionError as conn_err:
        print(f"Error connecting: {conn_err}")
    except requests.exceptions.Timeout as timeout_err:
        print(f"Timeout error occurred: {timeout_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"An error occurred: {req_err}")
    return None

def get_forecast(api_key, location, units='metric'):
    base_url = "http://api.openweathermap.org/data/2.5/forecast?"
    params = {
        'appid': api_key,
        'q': location,
        'units': units
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.ConnectionError as conn_err:
        print(f"Error connecting: {conn_err}")
    except requests.exceptions.Timeout as timeout_err:
        print(f"Timeout error occurred: {timeout_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"An error occurred: {req_err}")
    return None

def display_weather(data):
    if data:
        try:
            city = data['name']
            country = data['sys']['country']
            weather_desc = data['weather'][0]['description']
            temp = data['main']['temp']
            humidity = data['main']['humidity']

            print(f"Current weather in {city}, {country}:")
            print(f"Description: {weather_desc.capitalize()}")
            print(f"Temperature: {temp}°C")
            print(f"Humidity: {humidity}%")
        except KeyError as key_err:
            print(f"Key error: {key_err}. Invalid response structure.")
    else:
        print("No weather data to display.")

def display_forecast(data):
    if data:
        try:
            city = data['city']['name']
            country = data['city']['country']
            print(f"7-day weather forecast for {city}, {country}:")

            forecast_count = 7 * 8  # 7 days * 8 forecasts per day (every 3 hours)
            for forecast in data['list'][:forecast_count]:  
                dt_txt = forecast['dt_txt']
                weather_desc = forecast['weather'][0]['description']
                temp = forecast['main']['temp']
                humidity = forecast['main']['humidity']
                print(f"{dt_txt} - {weather_desc.capitalize()} | Temp: {temp}°C | Humidity: {humidity}%")
        except KeyError as key_err:
            print(f"Key error: {key_err}. Invalid response structure.")
    else:
        print("No forecast data to display.")

def main():
    load_dotenv()
    api_key = os.getenv('OPENWEATHERMAP_API_KEY')
    default_location = os.getenv('DEFAULT_LOCATION', '')
    if not api_key:
        print("Error: API key not found. Please set it in the .env file.")
        return

    while True:
        location = input(f"Enter a city name or ZIP code (or 'exit' to quit, default is {default_location}): ").strip()
        if location.lower() == 'exit':
            print("Exiting the weather program.")
            break
        if not location:
            location = default_location
        if not location:
            print("Please enter a valid city name or ZIP code.")
            continue

        unit = input("Choose units - 'C' for Celsius or 'F' for Fahrenheit (default is 'C'): ").strip().upper()
        units = 'imperial' if unit == 'F' else 'metric'

        choice = input("Do you want current weather or a 7-day forecast? (Enter 'current' or 'forecast'): ").strip().lower()
        
        if choice == 'forecast':
            forecast_data = get_forecast(api_key, location, units)
            display_forecast(forecast_data)
        else:
            weather_data = get_weather(api_key, location, units)
            display_weather(weather_data)

if __name__ == "__main__":
    main()
