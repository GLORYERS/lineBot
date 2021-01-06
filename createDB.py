import pandas as pd
import sqlite3

db = sqlite3.connect('rest.db')
dfs = pd.read_excel('rest.xlsx', sheet_name=None)
for table, df in dfs.items():
    df.to_sql(table, db)