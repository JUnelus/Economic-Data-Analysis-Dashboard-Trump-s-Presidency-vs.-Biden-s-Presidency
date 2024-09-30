import os
import json
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Create an SQLAlchemy engine and Connect to PostgreSQL
db_url = f"postgresql://{os.getenv('POSTGRES_USER')}:{os.getenv('POSTGRES_PASSWORD')}@{os.getenv('POSTGRES_HOST')}/{os.getenv('POSTGRES_DB')}"
engine = create_engine(db_url)

# Function to load JSON data and prepare DataFrame
def load_json_to_df(filename, indicator, presidency):
    with open(filename) as f:
        data = json.load(f)
    df = pd.DataFrame(data['observations'])
    df['indicator'] = indicator
    df['presidency'] = presidency
    df['value'] = df['value'].astype(float)
    df['date'] = pd.to_datetime(df['date'])
    return df[['date', 'value', 'indicator', 'presidency']]

# Load Trump's data
gdp_trump = load_json_to_df('gdp_trump.json', 'GDP', 'Trump')
unemployment_trump = load_json_to_df('unemployment_trump.json', 'Unemployment Rate', 'Trump')
cpi_trump = load_json_to_df('cpi_trump.json', 'CPI', 'Trump')

# Load Biden's data
gdp_biden = load_json_to_df('gdp_biden.json', 'GDP', 'Biden')
unemployment_biden = load_json_to_df('unemployment_biden.json', 'Unemployment Rate', 'Biden')
cpi_biden = load_json_to_df('cpi_biden.json', 'CPI', 'Biden')

# Concatenate all data
all_data = pd.concat([gdp_trump, unemployment_trump, cpi_trump, gdp_biden, unemployment_biden, cpi_biden])

# Insert data into PostgreSQL
all_data.to_sql('economic_data', engine, if_exists='replace', index=False)
