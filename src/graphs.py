import pandas as pd
import matplotlib.pyplot as plt
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv, dotenv_values
from datetime import datetime

def init():
    engine = create_engine('postgresql+psycopg2://'+os.getenv("DATABASE_USER"))

    tables = ['player','score','business']

    load_dotenv()

    dfs = {}
    for table in tables:
        dfs[table] = pd.read_sql_table(table, engine)
    
    return engine, dfs

def daily_uploads():
    engine, dfs = init()
    
    dates = dfs['score'][['upload_date','stage']]
    dates_stage_r = dates[dates['stage'] == 'R']
    dates_stage_s = dates[dates['stage'] == 'S']
    dates_r = dates_stage_r['upload_date'].dt.date
    dates_s = dates_stage_s['upload_date'].dt.date
    date_count_r = dates_r.value_counts()
    date_count_s = dates_s.value_counts()
    date_count_r = date_count_r.sort_index()
    date_count_s = date_count_s.sort_index()
    print(date_count_r)
    
    plt.figure(figsize=(10, 6))  # Set the figure size

    plt.plot(date_count_r.index, date_count_r, marker='o', linestyle='-', color='red')  # Plotting the data points
    plt.plot(date_count_s.index, date_count_s, marker='o', linestyle='-', color='blue')

    # Customize the plot
    plt.title('Line Graph of Value Over Time')  # Add title
    plt.xlabel('Date')  # Add x-axis label
    plt.ylabel('Value')  # Add y-axis label
    plt.grid(True)  # Add grid
    plt.xticks(rotation=45)  # Rotate x-axis labels for better readability

    plt.tight_layout()  # Adjust layout to prevent clipping of labels
    plt.show()  # Show the plot
    pass

# def avg_player

daily_uploads()