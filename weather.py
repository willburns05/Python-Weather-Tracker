import requests
import json
from datetime import datetime
import os
from dotenv import load_dotenv

def get_weather(city):
    """
    Get weather data for a given city using OpenWeatherMap API
    """
    # Add debug prints
    print("Current working directory:", os.getcwd())
    print("Files in directory:", os.listdir())
    
    load_dotenv()
    api_key = os.getenv('API_KEY')
    
    # Debug print for API key
    print("API Key found:", "Yes" if api_key else "No")
    if api_key:
        print("API Key value:", api_key)
    
    # If no API key is found, provide instructions
    if not api_key:
        print("\nAPI key not found. Please check:")
        print("1. Your .env file exists in the same folder as your script")
        print("2. Your .env file contains: API_KEY=your_key_here")
        print("3. There are no spaces or quotes in the .env file")
        return None
    
    # Make API request
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'  # Use metric units (Celsius)
    }
    
    try:
        response = requests.get(base_url, params=params)
        print("\nAPI Response Status:", response.status_code)  # Debug print
        response.raise_for_status()
        weather_data = response.json()
        
        # Extract relevant information
        temperature = weather_data['main']['temp']
        feels_like = weather_data['main']['feels_like']
        humidity = weather_data['main']['humidity']
        wind_speed = weather_data['wind']['speed']
        description = weather_data['weather'][0]['description']
        sunrise = datetime.fromtimestamp(weather_data['sys']['sunrise'])
        sunset = datetime.fromtimestamp(weather_data['sys']['sunset'])
        
        # Format and display weather information
        print("\nWeather in", city)
        print("=" * 30)
        print(f"Temperature: {temperature}°C")
        print(f"Feels like: {feels_like}°C")
        print(f"Conditions: {description.capitalize()}")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_speed} m/s")
        print(f"Sunrise: {sunrise.strftime('%H:%M')}")
        print(f"Sunset: {sunset.strftime('%H:%M')}")
        
    except requests.exceptions.RequestException as e:
        print(f"\nError fetching weather data: {e}")
    except KeyError as e:
        print(f"\nError parsing weather data: {e}")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")

def main():
    while True:
        city = input("\nEnter city name (or 'quit' to exit): ").strip()
        
        if city.lower() == 'quit':
            print("Goodbye!")
            break
            
        if city:
            get_weather(city)
        else:
            print("Please enter a valid city name.")

if __name__ == "__main__":
    main()