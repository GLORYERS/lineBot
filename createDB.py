import pandas as pd
import sqlite3

db = sqlite3.connect('./db/rest.db')
dfs = pd.read_excel('./db/rest.xlsx', sheet_name=None)
for table, df in dfs.items():
    df.to_sql(table, db)
