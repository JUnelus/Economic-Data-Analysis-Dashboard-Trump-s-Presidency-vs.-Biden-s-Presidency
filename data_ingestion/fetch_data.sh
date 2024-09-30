#!/bin/bash

# Get FRED API key from environment variable
API_KEY=os.getenv('FRED_API_KEY')

# Economic series IDs from FRED
GDP="GDP"
UNEMPLOYMENT_RATE="UNRATE"
CPI="CPIAUCSL"

# Set date ranges for Trump's and Biden's presidency
START_TRUMP="2017-01-20"
END_TRUMP="2021-01-19"
START_BIDEN="2021-01-20"
END_BIDEN="2024-09-01"

# Fetch data from FRED using curl
curl -o gdp_trump.json "https://api.stlouisfed.org/fred/series/observations?series_id=$GDP&api_key=$API_KEY&file_type=json&observation_start=$START_TRUMP&observation_end=$END_TRUMP"
curl -o gdp_biden.json "https://api.stlouisfed.org/fred/series/observations?series_id=$GDP&api_key=$API_KEY&file_type=json&observation_start=$START_BIDEN&observation_end=$END_BIDEN"

curl -o unemployment_trump.json "https://api.stlouisfed.org/fred/series/observations?series_id=$UNEMPLOYMENT_RATE&api_key=$API_KEY&file_type=json&observation_start=$START_TRUMP&observation_end=$END_TRUMP"
curl -o unemployment_biden.json "https://api.stlouisfed.org/fred/series/observations?series_id=$UNEMPLOYMENT_RATE&api_key=$API_KEY&file_type=json&observation_start=$START_BIDEN&observation_end=$END_BIDEN"

curl -o cpi_trump.json "https://api.stlouisfed.org/fred/series/observations?series_id=$CPI&api_key=$API_KEY&file_type=json&observation_start=$START_TRUMP&observation_end=$END_TRUMP"
curl -o cpi_biden.json "https://api.stlouisfed.org/fred/series/observations?series_id=$CPI&api_key=$API_KEY&file_type=json&observation_start=$START_BIDEN&observation_end=$END_BIDEN"
