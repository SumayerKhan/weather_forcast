# Weather Forecast Application - Main Interface

# This is the main Streamlit application that provides a web-based interface
# for displaying weather forecasts. Users can input a city name, select forecast
# duration, and choose between temperature charts and sky condition visualizations.

# The application fetches real-time weather data from OpenWeatherMap API and
# presents it in an intuitive, interactive format.

# Dependencies:
#     - streamlit: Web application framework for the user interface
#     - plotly.express: Interactive plotting library for temperature charts
#     - backend: Custom module for weather data fetching

# Features:
#     - City-based weather search
#     - 1-5 day forecast selection
#     - Temperature trend visualization
#     - Sky condition icons display
#     - Error handling for invalid cities

# Author: Sumayer Khan Sajid
# Date: 17/09/2025

import streamlit as st
import plotly.express as px 
from backend import get_data

# Configure the main page layout and title
st.title("Weather Forcast For The Next Days")

# User Input Section
# =================

# Text input for city/location name
# Users can enter any city name, optionally with country code for specificity
place = st.text_input("Place: ")

# Slider for selecting forecast duration
# Range: 1-5 days (limited by OpenWeatherMap free tier)
# Default: 1 day
days = st.slider("Forcast Days: ", 
                 min_value=1,
                 max_value=5,
                 value=1,
                 help="Select the number of forcasted days.")

# Dropdown for selecting data visualization type
# Temperature: Shows line chart of temperature trends
# Sky: Shows weather condition icons with timestamps
option = st.selectbox("Select Data to view: ", ("Temperature", "Sky"))

# Display subheader with current selection summary
st.subheader(f"{option} for the next {days} days in {place}")

# Main Application Logic
# =====================

# Only proceed if user has entered a city name
if place:
    try: 
        # Fetch weather data using the backend module
        # This returns a list of forecast data points (8 per day)
        filtered_data = get_data(place, days)
        
        # Temperature Visualization Branch
        # ===============================
        if option == "Temperature":

            # Process and display temperature data as an interactive line chart.
            
            # Data Processing:
            # - Extract temperature values from API response (in Kelvin)
            # - Convert temperatures by dividing by 10 (Note: This may need adjustment)
            # - Extract corresponding datetime strings for x-axis
            
            # Visualization:
            # - Create line chart using Plotly Express
            # - X-axis: Date/time progression
            # - Y-axis: Temperature in Celsius

            
            temperature = [(entry["main"]["temp"]) for entry in filtered_data]
            
            # Extract datetime strings for chart x-axis labels
            dates = [entry["dt_txt"] for entry in filtered_data]
            
            # Create interactive line chart using Plotly
            figure = px.line(x=dates, 
                           y=temperature,
                           labels={"x": "Date", "y": "Temperatures (C)"})
            
            # Display the chart in the Streamlit interface
            st.plotly_chart(figure)

        # Sky Conditions Visualization Branch
        # ==================================
        if option == "Sky":
            # Display weather conditions using icons with timestamps.
            
            # Process:
            # - Map weather conditions to appropriate icon file paths
            # - Extract weather condition data from API response
            # - Display icons in a grid layout with timestamp captions
            
            # Icon Mapping:
            # - Clear: clear.png (sunny/clear sky)
            # - Clouds: cloud.png (cloudy conditions)
            # - Rain: rain.png (rainy weather)
            # - Snow: snow.png (snowy conditions)

            
            # Define mapping between weather conditions and icon file paths
            # Icons should be stored in the 'images/' directory
            images = {"Clear": "images/clear.png",
                     "Clouds": "images/cloud.png",
                     "Rain": "images/rain.png",
                     "Snow": "images/snow.png"}
            
            # Extract weather condition for each forecast entry
            # Uses the main weather category (Clear, Clouds, Rain, Snow)
            sky = [entry["weather"][0]["main"] for entry in filtered_data]
            
            # Map weather conditions to corresponding image file paths
            image_paths = [images[condition] for condition in sky]
            
            # Extract datetime strings for image captions
            caption = [entry["dt_txt"] for entry in filtered_data]
            
            # Display weather condition images with timestamps
            # width=115: Sets consistent icon size
            # caption: Shows date/time below each icon
            st.image(image_paths, width=115, caption=caption)
            
    except KeyError as e:
        # Handle cases where the city is not found or API response is invalid.
        
        # Common causes:
        # - Misspelled city name
        # - City not in OpenWeatherMap database
        # - API response structure changed
        # - Network connectivity issues
        st.error("City not found. Please try again.")