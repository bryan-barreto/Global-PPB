import pandas as pd
import matplotlib.pyplot as py
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv, dotenv_values

engine = create_engine('postgresql+psycopg2://'+os.getenv("DATABASE_USER"))

tables = ['player','score','business']

load_dotenv()

dfs = {}
for table in tables:
    dfs[table] = pd.read_sql_table(table, engine)

