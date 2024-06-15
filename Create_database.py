import pandas as pd
import sqlite3

# Read the CSV file into a DataFrame
circuits_df = pd.read_csv('archive/circuits.csv')

# Connect to sql database or create one if table doesn't exist
conn = sqlite3.connect('Greatest.db')

# Create a cursor object to execute SQL commands
cur = conn.cursor()

# Read the CSV file into a DataFrame
constructor_results_df = pd.read_csv('archive/constructor_results.csv')
cur.execute('''
    CREATE TABLE IF NOT EXISTS Constructor_results (
   constructorResultsId INTEGER,
   raceId INTEGER,
   constructorId INTEGER,
   points INTEGER,
   status TEXT
    )
''')

# Insert Data into the table
for index, row in constructor_results_df.iterrows():
    cur.execute('''
        INSERT INTO Constructor_results(constructorResultsId, raceId, constructorId, points, status)
        VALUES(?, ?, ?, ?, ?)
        ''', (row['constructorResultsId'], row['raceId'], row['constructorId'], row['points'], row['status']))
# cur.execute('''
#     CREATE TABLE IF NOT EXISTS Circuits (
#     circuitId INTEGER,
#     circuitRef TEXT,
#     name TEXT,
#     location TEXT,
#     country TEXT,
#     lat REAL,
#     lng REAL,
#     alt REAL,
#     url TEXT
#     )
# ''')
#
# # Insert Data into the table
# for index, row in circuits_df.iterrows():
#     cur.execute('''
#         INSERT INTO Circuits(circuitId, circuitRef, name,location, country, lat, lng, alt, url)
#         VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)
#         ''', (row['circuitId'], row['circuitRef'], row['name'], row['location'], row['country'], row['lat'], row['lng'], row['alt'], row['url']))
# cur.execute('''
#     CREATE TABLE IF NOT EXISTS Circuits (
#     circuitId INTEGER,
#     circuitRef TEXT,
#     name TEXT,
#     location TEXT,
#     country TEXT,
#     lat REAL,
#     lng REAL,
#     alt REAL,
#     url TEXT
#     )
# ''')
#
# # Insert Data into the table
# for index, row in circuits_df.iterrows():
#     cur.execute('''
#         INSERT INTO Circuits(circuitId, circuitRef, name,location, country, lat, lng, alt, url)
#         VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)
#         ''', (row['circuitId'], row['circuitRef'], row['name'], row['location'], row['country'], row['lat'], row['lng'], row['alt'], row['url']))
# cur.execute('''
#     CREATE TABLE IF NOT EXISTS Circuits (
#     circuitId INTEGER,
#     circuitRef TEXT,
#     name TEXT,
#     location TEXT,
#     country TEXT,
#     lat REAL,
#     lng REAL,
#     alt REAL,
#     url TEXT
#     )
# ''')
#
# # Insert Data into the table
# for index, row in circuits_df.iterrows():
#     cur.execute('''
#         INSERT INTO Circuits(circuitId, circuitRef, name,location, country, lat, lng, alt, url)
#         VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)
#         ''', (row['circuitId'], row['circuitRef'], row['name'], row['location'], row['country'], row['lat'], row['lng'], row['alt'], row['url']))
# cur.execute('''
#     CREATE TABLE IF NOT EXISTS Circuits (
#     circuitId INTEGER,
#     circuitRef TEXT,
#     name TEXT,
#     location TEXT,
#     country TEXT,
#     lat REAL,
#     lng REAL,
#     alt REAL,
#     url TEXT
#     )
# ''')
#
# # Insert Data into the table
# for index, row in circuits_df.iterrows():
#     cur.execute('''
#         INSERT INTO Circuits(circuitId, circuitRef, name,location, country, lat, lng, alt, url)
#         VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)
#         ''', (row['circuitId'], row['circuitRef'], row['name'], row['location'], row['country'], row['lat'], row['lng'], row['alt'], row['url']))
# cur.execute('''
#     CREATE TABLE IF NOT EXISTS Circuits (
#     circuitId INTEGER,
#     circuitRef TEXT,
#     name TEXT,
#     location TEXT,
#     country TEXT,
#     lat REAL,
#     lng REAL,
#     alt REAL,
#     url TEXT
#     )
# ''')
#
# # Insert Data into the table
# for index, row in circuits_df.iterrows():
#     cur.execute('''
#         INSERT INTO Circuits(circuitId, circuitRef, name,location, country, lat, lng, alt, url)
#         VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)
#         ''', (row['circuitId'], row['circuitRef'], row['name'], row['location'], row['country'], row['lat'], row['lng'], row['alt'], row['url']))
# cur.execute('''
#     CREATE TABLE IF NOT EXISTS Circuits (
#     circuitId INTEGER,
#     circuitRef TEXT,
#     name TEXT,
#     location TEXT,
#     country TEXT,
#     lat REAL,
#     lng REAL,
#     alt REAL,
#     url TEXT
#     )
# ''')
#
# # Insert Data into the table
# for index, row in circuits_df.iterrows():
#     cur.execute('''
#         INSERT INTO Circuits(circuitId, circuitRef, name,location, country, lat, lng, alt, url)
#         VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)
#         ''', (row['circuitId'], row['circuitRef'], row['name'], row['location'], row['country'], row['lat'], row['lng'], row['alt'], row['url']))
# cur.execute('''
#     CREATE TABLE IF NOT EXISTS Circuits (
#     circuitId INTEGER,
#     circuitRef TEXT,
#     name TEXT,
#     location TEXT,
#     country TEXT,
#     lat REAL,
#     lng REAL,
#     alt REAL,
#     url TEXT
#     )
# ''')
#
# # Insert Data into the table
# for index, row in circuits_df.iterrows():
#     cur.execute('''
#         INSERT INTO Circuits(circuitId, circuitRef, name,location, country, lat, lng, alt, url)
#         VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)
#         ''', (row['circuitId'], row['circuitRef'], row['name'], row['location'], row['country'], row['lat'], row['lng'], row['alt'], row['url']))
# cur.execute('''
#     CREATE TABLE IF NOT EXISTS Circuits (
#     circuitId INTEGER,
#     circuitRef TEXT,
#     name TEXT,
#     location TEXT,
#     country TEXT,
#     lat REAL,
#     lng REAL,
#     alt REAL,
#     url TEXT
#     )
# ''')
#
# # Insert Data into the table
# for index, row in circuits_df.iterrows():
#     cur.execute('''
#         INSERT INTO Circuits(circuitId, circuitRef, name,location, country, lat, lng, alt, url)
#         VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)
#         ''', (row['circuitId'], row['circuitRef'], row['name'], row['location'], row['country'], row['lat'], row['lng'], row['alt'], row['url']))
# cur.execute('''
#     CREATE TABLE IF NOT EXISTS Circuits (
#     circuitId INTEGER,
#     circuitRef TEXT,
#     name TEXT,
#     location TEXT,
#     country TEXT,
#     lat REAL,
#     lng REAL,
#     alt REAL,
#     url TEXT
#     )
# ''')
#
# # Insert Data into the table
# for index, row in circuits_df.iterrows():
#     cur.execute('''
#         INSERT INTO Circuits(circuitId, circuitRef, name,location, country, lat, lng, alt, url)
#         VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)
#         ''', (row['circuitId'], row['circuitRef'], row['name'], row['location'], row['country'], row['lat'], row['lng'], row['alt'], row['url']))
# cur.execute('''
#     CREATE TABLE IF NOT EXISTS Circuits (
#     circuitId INTEGER,
#     circuitRef TEXT,
#     name TEXT,
#     location TEXT,
#     country TEXT,
#     lat REAL,
#     lng REAL,
#     alt REAL,
#     url TEXT
#     )
# ''')
#
# # Insert Data into the table
# for index, row in circuits_df.iterrows():
#     cur.execute('''
#         INSERT INTO Circuits(circuitId, circuitRef, name,location, country, lat, lng, alt, url)
#         VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)
#         ''', (row['circuitId'], row['circuitRef'], row['name'], row['location'], row['country'], row['lat'], row['lng'], row['alt'], row['url']))
# cur.execute('''
#     CREATE TABLE IF NOT EXISTS Circuits (
#     circuitId INTEGER,
#     circuitRef TEXT,
#     name TEXT,
#     location TEXT,
#     country TEXT,
#     lat REAL,
#     lng REAL,
#     alt REAL,
#     url TEXT
#     )
# ''')
#
# # Insert Data into the table
# for index, row in circuits_df.iterrows():
#     cur.execute('''
#         INSERT INTO Circuits(circuitId, circuitRef, name,location, country, lat, lng, alt, url)
#         VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)
#         ''', (row['circuitId'], row['circuitRef'], row['name'], row['location'], row['country'], row['lat'], row['lng'], row['alt'], row['url']))
# cur.execute('''
#     CREATE TABLE IF NOT EXISTS Circuits (
#     circuitId INTEGER,
#     circuitRef TEXT,
#     name TEXT,
#     location TEXT,
#     country TEXT,
#     lat REAL,
#     lng REAL,
#     alt REAL,
#     url TEXT
#     )
# ''')
#
# # Insert Data into the table
# for index, row in circuits_df.iterrows():
#     cur.execute('''
#         INSERT INTO Circuits(circuitId, circuitRef, name,location, country, lat, lng, alt, url)
#         VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)
#         ''', (row['circuitId'], row['circuitRef'], row['name'], row['location'], row['country'], row['lat'], row['lng'], row['alt'], row['url']))
# cur.execute('''
#     CREATE TABLE IF NOT EXISTS Circuits (
#     circuitId INTEGER,
#     circuitRef TEXT,
#     name TEXT,
#     location TEXT,
#     country TEXT,
#     lat REAL,
#     lng REAL,
#     alt REAL,
#     url TEXT
#     )
# ''')
#
# # Insert Data into the table
# for index, row in circuits_df.iterrows():
#     cur.execute('''
#         INSERT INTO Circuits(circuitId, circuitRef, name,location, country, lat, lng, alt, url)
#         VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)
#         ''', (row['circuitId'], row['circuitRef'], row['name'], row['location'], row['country'], row['lat'], row['lng'], row['alt'], row['url']))
# cur.execute('''
#     CREATE TABLE IF NOT EXISTS Circuits (
#     circuitId INTEGER,
#     circuitRef TEXT,
#     name TEXT,
#     location TEXT,
#     country TEXT,
#     lat REAL,
#     lng REAL,
#     alt REAL,
#     url TEXT
#     )
# ''')
#
# # Insert Data into the table
# for index, row in circuits_df.iterrows():
#     cur.execute('''
#         INSERT INTO Circuits(circuitId, circuitRef, name,location, country, lat, lng, alt, url)
#         VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)
#         ''', (row['circuitId'], row['circuitRef'], row['name'], row['location'], row['country'], row['lat'], row['lng'], row['alt'], row['url']))
#
# Commit the action
conn.commit()

# Close the cursor and connection
cur.close()
conn.close()
