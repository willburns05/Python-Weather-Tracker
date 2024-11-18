# Weather CLI Application

A command-line Python application that retrieves real-time weather information for a specified city using the OpenWeatherMap API.

## Features

- Retrieves current weather details such as temperature, humidity, wind speed, and conditions.
- Provides sunrise and sunset times.
- Uses the OpenWeatherMap API for reliable and up-to-date data.
- Accepts user input for city names in a loop until the user exits.
- Includes error handling for API requests, data parsing, and missing API key configurations.

---

## How to Use

### Prerequisites

1. Python 3.x installed on your system.
2. An OpenWeatherMap API key. Sign up at [OpenWeatherMap](https://openweathermap.org/) to get your API key.
3. Install the required dependencies by running:

   pip install -r requirements.txt

### Setup Instructions
Clone this repository or download the script file.

Create a .env file in the same directory as the script and add your OpenWeatherMap API key in the following format:

plaintext
Copy code
API_KEY=your_api_key_here
Run the script:

bash
Copy code
python weather.py
Enter the name of the city you want to fetch weather data for. Type quit to exit the application.

### Debugging Tips
Ensure your .env file is correctly configured with the API_KEY.
The script prints helpful debug information, such as the current working directory and API key detection status, for troubleshooting.
Check the status code of the API response for further insights (e.g., 401 Unauthorized if the API key is incorrect).