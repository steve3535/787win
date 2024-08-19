import pandas as pd
import sqlite3

df = pd.read_csv('data/players.csv')

# Create a SQLite database and write the data to a table
connection = sqlite3.connect("data/players.db")
df.to_sql(name="players", con=connection, if_exists='replace', index=False)

