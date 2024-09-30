import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# FRED API key
API_KEY = os.getenv('FRED_API_KEY')

# Economic series IDs from FRED
GDP = 'GDP'
UNEMPLOYMENT_RATE = 'UNRATE'
CPI = 'CPIAUCSL'

# Set date ranges for Trump's and Biden's presidency
START_TRUMP = '2017-01-20'
END_TRUMP = '2021-01-19'
START_BIDEN = '2021-01-20'
END_BIDEN = '2024-09-01'


# Fetch data function
def fetch_fred_data(series_id, start_date, end_date, filename):
    url = f'https://api.stlouisfed.org/fred/series/observations'
    params = {
        'series_id': series_id,
        'api_key': API_KEY,
        'file_type': 'json',
        'observation_start': start_date,
        'observation_end': end_date
    }
    response = requests.get(url, params=params)
    with open(filename, 'w') as f:
        f.write(response.text)


# Fetch data for Trump and Biden
fetch_fred_data(GDP, START_TRUMP, END_TRUMP, 'gdp_trump.json')
fetch_fred_data(GDP, START_BIDEN, END_BIDEN, 'gdp_biden.json')

fetch_fred_data(UNEMPLOYMENT_RATE, START_TRUMP, END_TRUMP, 'unemployment_trump.json')
fetch_fred_data(UNEMPLOYMENT_RATE, START_BIDEN, END_BIDEN, 'unemployment_biden.json')

fetch_fred_data(CPI, START_TRUMP, END_TRUMP, 'cpi_trump.json')
fetch_fred_data(CPI, START_BIDEN, END_BIDEN, 'cpi_biden.json')

print("Data fetched and saved successfully.")
