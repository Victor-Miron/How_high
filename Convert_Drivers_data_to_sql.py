import sqlite3
import pandas as pd

# Connect Database to sqlite

conn = sqlite3.connect("Greatest.db")

# Load data into a panda Dataframe
df = pd.read_sql_query("SELECT * FROM 'Drivers Data'", conn)

# Close conn
conn.close()

# Save data to a CSV file
df.to_csv('Drivers_data_tableau_update.csv', index=False)
