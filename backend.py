# Weather Data Backend Module

# This module handles weather data fetching and processing from the OpenWeatherMap API.
# It provides functions to retrieve forecast data for specified locations and time periods.

# Dependencies:
#     - requests: For making HTTP API calls
#     - os: For environment variable access
#     - python-dotenv: For loading environment variables from .env file

# Author: Sumayer Khan
# Date: 17/09/2025

import requests
import os
from dotenv import load_dotenv
import streamlit as st

# Load environment variables from .env file
load_dotenv()

# Retrieve the OpenWeatherMap API key from environment variables
# This key should be stored in a .env file as: API_KEY=your_api_key_here
# Try Streamlit secrets if available
try:
    _SECRET_API_KEY = st.secrets.get("API_KEY")
except Exception:
    _SECRET_API_KEY = None

# Fallback to environment variable
API_KEY = _SECRET_API_KEY or os.getenv("API_KEY")


def get_data(place, forcast_days):
    # """
    # Fetches weather forecast data for a specified location and number of days.
    
    # This function makes an API call to OpenWeatherMap's 5-day weather forecast API
    # and returns filtered data based on the requested forecast duration.
    
    # Args:
    #     place (str): The name of the city/location for which to fetch weather data.
    #                 Can include country code for specificity (e.g., "London,UK").
    #     forcast_days (int): Number of days for the forecast (1-5 days).
    #                        Each day contains 8 data points (every 3 hours).
    
    # Returns:
    #     list: A list of dictionaries containing weather data. Each dictionary
    #           represents one 3-hour forecast period with the following structure:
    #           - dt: Unix timestamp
    #           - dt_txt: Date and time in text format
    #           - main: Temperature, pressure, humidity data
    #           - weather: Weather conditions and descriptions
    #           - clouds, wind, visibility: Additional weather parameters
    
    # Raises:
    #     requests.exceptions.RequestException: If the API request fails
    #     KeyError: If the API response doesn't contain expected data structure
        
    # Example:
    #     >>> data = get_data("Tokyo", 3)
    #     >>> len(data)  # Should return 24 (8 data points × 3 days)
    #     24
    #     >>> data[0]["main"]["temp"]  # Temperature in Kelvin
    #     298.15
    
    # Note:
    #     - The OpenWeatherMap API returns temperature in Celsius
    #     - Free tier API provides forecasts up to 5 days
    #     - Data points are provided every 3 hours (8 per day)
    #     - Requires a valid API key in environment variables

    # Construct the API URL with the place parameter and API key
    # Using the 5-day weather forecast endpoint
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}&units=metric"
    
    # Make the HTTP GET request to the OpenWeatherMap API
    response = requests.get(url)
    
    # Parse the JSON response into a Python dictionary
    data = response.json()
    
    # Extract the forecast list from the response
    # The "list" key contains all forecast data points
    filtered_data = data["list"]
    
    # Calculate the number of data points needed
    # OpenWeatherMap provides 8 data points per day (every 3 hours)
    nr_values = 8 * forcast_days
    
    # Slice the data to get only the requested number of forecast days
    filtered_data = filtered_data[:nr_values]

    return filtered_data


# Main execution block for testing purposes
if __name__ == "__main__":
    # Test block to verify the get_data function works correctly.
    
    # This section runs only when the script is executed directly (not imported).
    # It tests the function with Tokyo as the location and 3 days forecast,
    # then prints the number of data points returned.
    
    # Expected output: 24 (8 data points per day × 3 days)
    
    # Note: The original code had an extra 'kind' parameter that's not used
    # in the function definition - this has been removed for consistency.
    
    try:
        # Test the function with sample parameters
        test_data = get_data(place="Tokyo", forcast_days=3)
        print(f"Number of data points retrieved: {len(test_data)}")
        
        # Optional: Print first data point structure for verification
        if test_data:
            print("Sample data point structure:")
            print(f"Date/Time: {test_data[0]['dt_txt']}")
            print(f"Temperature (K): {test_data[0]['main']['temp']}")
            print(f"Weather: {test_data[0]['weather'][0]['main']}")
            
    except Exception as e:
        print(f"Error testing get_data function: {e}")
        print("Please check your API key and internet connection.")