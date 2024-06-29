import sqlite3

# Connect to the SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('Greatest.db')

# Create a cursor object to execute SQL commands
cur = conn.cursor()

# Select columns from different tables and create the table Constructor Data
cur.execute(''' 
    CREATE TABLE IF NOT EXISTS "Constructor Data" AS
        SELECT Constructors.name, Constructors.nationality, 
               "Constructor standings".points, "Constructor standings".position, 
               "Constructor standings".wins, 
               "Constructor results".points,
               Results.number, Results.grid, Results.position,
               Circuits.name AS circuit_name, Circuits.location, Circuits.country,
               Races.name AS race_name, Races.date, 
               Seasons.year
        FROM Constructors
        INNER JOIN "Constructor standings" ON "Constructor standings".constructorId = Constructors.constructorId
        INNER JOIN "Constructor results" ON "Constructor results".constructorId = Constructors.constructorId
        INNER JOIN Results ON Results.constructorId = Constructors.constructorId
        INNER JOIN Races ON Races.raceId = Results.raceId
        INNER JOIN Circuits ON Circuits.circuitId = Races.circuitId
        INNER JOIN Seasons ON Seasons.year = Races.year;
''')

# Commit the transaction
conn.commit()

# Close the cursor and connection
cur.close()
conn.close()
