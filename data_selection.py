import sqlite3
import pandas as pd
# Connect to the SQLite database
conn = sqlite3.connect('Greatest.db')  # Replace 'your_database.db' with your database file

# Query the database
first_two = '''
SELECT name, sum(wins) AS "Total wins", MIN(year) AS "Year started", max(year) AS "Year ended",
       (max(year) - min(year)) AS "Total years"
FROM "Constructor Data"
GROUP by name
ORDER by "Total wins" DESC
LIMIT 2;
'''
df = pd.read_sql_query(query, conn)

# Close the database connection
conn.close()

