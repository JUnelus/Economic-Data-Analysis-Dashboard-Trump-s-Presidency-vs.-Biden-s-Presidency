import os
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Create an SQLAlchemy engine and Connect to PostgreSQL
db_url = f"postgresql://{os.getenv('POSTGRES_USER')}:{os.getenv('POSTGRES_PASSWORD')}@{os.getenv('POSTGRES_HOST')}/{os.getenv('POSTGRES_DB')}"
engine = create_engine(db_url)

# Query data from PostgreSQL
query = """
SELECT * FROM economic_data WHERE indicator IN ('GDP', 'Unemployment Rate', 'CPI')
"""
df = pd.read_sql(query, engine)

# Check for missing values
print(df.isnull().sum())

# Perform any necessary data cleaning
df = df.dropna()  # Drop rows with missing values

# Convert 'value' column to numeric (just in case)
df['value'] = pd.to_numeric(df['value'])

# Group data by presidency and indicator for summary statistics
summary = df.groupby(['presidency', 'indicator'])['value'].agg(['mean', 'max', 'min'])
print(summary)
