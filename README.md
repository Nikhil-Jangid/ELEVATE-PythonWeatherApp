# PythonWeatherApp

PythonWeatherApp is a simple console-based application that fetches and displays current weather conditions and a 7-day forecast using the OpenWeatherMap API. Users can input a city name or ZIP code to get real-time weather information, including temperature, humidity, and a brief description of the weather.

## Features

- Fetch current weather data based on city name or ZIP code.
- Display temperature, humidity, and weather description.
- Provide a 7-day weather forecast.
- Allow users to choose between Celsius and Fahrenheit units.
- Handle invalid inputs and API errors gracefully.
- Easy-to-use command-line interface.

## Requirements

- Python 3.x
- `requests` library
- `python-dotenv` library

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/Nikhil-Jangid/ELEVATE-PythonWeatherApp.git
    cd ELEVATE-PythonWeatherApp
    ```

2. Install the required libraries:
    ```sh
    pip install requests python-dotenv
    ```

3. Create a `.env` file in the root directory of the project and add your OpenWeatherMap API key:
    ```env
    OPENWEATHERMAP_API_KEY=your_openweathermap_api_key
    ```

    Optionally, you can set a default location:
    ```env
    DEFAULT_LOCATION=your_default_location
    ```

## Usage

1. Run the script:
    ```sh
    python weather_app.py
    ```

2. Follow the prompts:
    - Enter a city name or ZIP code (or press Enter to use the default location if set).
    - Choose units - 'C' for Celsius or 'F' for Fahrenheit (default is 'C').
    - Choose between current weather or a 7-day forecast.


## Example

\`\`\`
Enter a city name or ZIP code (or 'exit' to quit, default is your_default_location): New York
Choose units - 'C' for Celsius or 'F' for Fahrenheit (default is 'C'): C
Do you want current weather or a 7-day forecast? (Enter 'current' or 'forecast'): forecast
7-day weather forecast for New York, US:
2024-06-20 15:00:00 - Clear sky | Temp: 27.5°C | Humidity: 55%
2024-06-20 18:00:00 - Few clouds | Temp: 26.3°C | Humidity: 60%
...
\`\`\`

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request if you have any improvements or suggestions.

## Acknowledgments

- [OpenWeatherMap](https://openweathermap.org/) for providing the weather data API.
- [python-dotenv](https://github.com/theskumar/python-dotenv) for managing environment variables.
EOL
