# Weather Forecast Application 🌤️

A simple and intuitive weather forecasting application built with Streamlit that displays temperature trends and sky conditions for any city worldwide.

## Features

- **Interactive City Search**: Enter any city name to get weather forecasts
- **Flexible Time Range**: Choose forecast duration from 1 to 5 days
- **Dual View Options**:
  - **Temperature View**: Line chart showing temperature trends in Celsius over time
  - **Sky Conditions View**: Visual representation of weather conditions with icons
- **Real-time Data**: Fetches live weather data from OpenWeatherMap API with metric units
- **User-friendly Interface**: Clean, responsive Streamlit-based UI


## Installation

### Prerequisites

- Python 3.7 or higher
- OpenWeatherMap API key (free registration required)

### Setup Steps

1. **Clone or download the project files**
   ```bash
   # Ensure you have these files:
   # - main.py
   # - backend.py
   # - .env (you'll create this)
   # - images/ folder with weather icons
   ```

2. **Install required packages**
   
   **Option A: Using requirements.txt (Recommended)**
   ```bash
   pip install -r requirements.txt
   ```
   
   **Option B: Manual installation**
   ```bash
   pip install streamlit plotly requests python-dotenv
   ```

3. **Get OpenWeatherMap API Key**
   - Visit [OpenWeatherMap](https://openweathermap.org/api)
   - Sign up for a free account
   - Generate your API key from the dashboard

4. **Configure Environment Variables**
   Create a `.env` file in the project root:
   ```
   API_KEY=your_openweathermap_api_key_here
   ```

5. **Prepare Weather Icons**
   Create an `images/` folder with these icon files:
   - `clear.png` - for clear/sunny weather
   - `cloud.png` - for cloudy conditions
   - `rain.png` - for rainy weather
   - `snow.png` - for snowy conditions

## Usage

1. **Start the application**
   ```bash
   streamlit run main.py
   ```

2. **Access the web interface**
   - Open your browser to `http://localhost:8501`
   - The application will load with the weather forecast interface

3. **Using the App**
   - Enter a city name in the text input field
   - Adjust the forecast days using the slider (1-5 days)
   - Select either "Temperature" or "Sky" from the dropdown
   - View the results automatically displayed below

## How It Works

### Data Flow
1. User inputs city name and selects preferences
2. `backend.py` makes API call to OpenWeatherMap
3. Raw weather data is filtered and processed
4. `main.py` renders the data as charts or images
5. Results display in the Streamlit interface

### API Integration
- Uses OpenWeatherMap 5-day forecast API with metric units
- Data points every 3 hours (8 data points per day)
- Temperature returned directly in Celsius (no conversion needed)
- Weather conditions mapped to appropriate icons

## File Structure

```
weather-app/
│
├── main.py              # Streamlit frontend application
├── backend.py           # Weather data fetching and processing
├── requirements.txt     # Python dependencies
├── .env                 # Environment variables (API key)
└── images/             # Weather condition icons
    ├── clear.png
    ├── cloud.png
    ├── rain.png
    └── snow.png
```

## Technical Details

### Dependencies
- **Streamlit**: Web app framework for the user interface
- **Plotly Express**: Interactive charting for temperature visualization
- **Requests**: HTTP library for API calls
- **python-dotenv**: Environment variable management

### Complete Dependencies List
The `requirements.txt` file includes all necessary packages with their versions:
- streamlit==1.49.1
- plotly==6.3.0
- requests==2.32.5
- python-dotenv==1.1.1
- And other supporting packages for full functionality

### API Specifications
- **Endpoint**: OpenWeatherMap 5-day weather forecast with metric units
- **Update Frequency**: Every 3 hours
- **Data Format**: JSON response with weather parameters in Celsius
- **Rate Limits**: Free tier allows 1000 calls/day

## Troubleshooting

### Common Issues

**"City not found" error**
- Verify the city name spelling
- Try including country code (e.g., "London,UK")
- Check internet connection

**API key errors**
- Ensure `.env` file exists with correct `API_KEY`
- Verify your OpenWeatherMap API key is active
- Check for any extra spaces in the `.env` file

**Missing weather icons**
- Ensure `images/` folder exists in the project directory
- Verify all four icon files are present and named correctly
- Check file permissions

**Temperature displaying incorrectly**
- Temperature is now returned directly in Celsius from API
- If temperatures seem off, verify your API key and internet connection
- Check that the API response structure matches expectations

## Customization Options

### Extending Forecast Days
- Modify the slider's `max_value` in `main.py`
- Note: OpenWeatherMap free tier provides 5-day forecasts

### Adding Weather Parameters
- Extend the selectbox options (humidity, pressure, wind speed)
- Modify `backend.py` to extract additional data fields
- Update visualization logic in `main.py`

### Styling Improvements
- Customize Streamlit themes
- Modify chart colors and styling
- Add CSS styling with `st.markdown`

## Contributing

Feel free to submit issues and enhancement requests! Areas for improvement:
- Error handling enhancements
- Additional weather parameters
- Improved icon/styling system
- Data caching for better performance

## License

**Author**: Sumayer Khan Sajid  
**Date**: September 17, 2025

---

**Note**: Remember to keep your API key secure and never commit it to version control!
