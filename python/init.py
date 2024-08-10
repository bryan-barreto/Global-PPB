from sqlalchemy import create_engine
import os
from dotenv import load_dotenv
import pandas as pd


def init():
    load_dotenv()

    engine = create_engine('postgresql+psycopg2://'+os.getenv("DATABASE_USER"))

    tables = ['player','score','business']
    

    dfs = {}
    for table in tables:
        dfs[table] = pd.read_sql_table(table, engine)
    return engine, dfs