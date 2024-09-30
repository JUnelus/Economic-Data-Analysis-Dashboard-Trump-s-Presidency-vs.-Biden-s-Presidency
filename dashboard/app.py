import os
import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Create an SQLAlchemy engine and Connect to PostgreSQL
db_url = f"postgresql://{os.getenv('POSTGRES_USER')}:{os.getenv('POSTGRES_PASSWORD')}@{os.getenv('POSTGRES_HOST')}/{os.getenv('POSTGRES_DB')}"
engine = create_engine(db_url)
query = """
SELECT * FROM economic_data WHERE indicator IN ('GDP', 'Unemployment Rate', 'CPI')
"""
df = pd.read_sql(query, engine)

# Initialize Dash app
app = dash.Dash(__name__)

# Create figures for each economic indicator
fig_gdp = px.line(df[df['indicator'] == 'GDP'], x='date', y='value', color='presidency',
                  title='GDP Comparison: Trump vs. Biden')
fig_unemployment = px.line(df[df['indicator'] == 'Unemployment Rate'], x='date', y='value', color='presidency',
                           title='Unemployment Rate Comparison: Trump vs. Biden')
fig_cpi = px.line(df[df['indicator'] == 'CPI'], x='date', y='value', color='presidency',
                  title='CPI Comparison: Trump vs. Biden')

# Dash layout
app.layout = html.Div(children=[
    html.H1(children='Economic Data Analysis Dashboard: Trump vs. Biden'),

    dcc.Graph(
        id='gdp-graph',
        figure=fig_gdp
    ),

    dcc.Graph(
        id='unemployment-graph',
        figure=fig_unemployment
    ),

    dcc.Graph(
        id='cpi-graph',
        figure=fig_cpi
    )
])

# Run Dash app
if __name__ == '__main__':
    app.run_server(debug=True)
