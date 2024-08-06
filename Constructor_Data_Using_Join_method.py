import sqlite3

# Connect to the SQLite database (or create it if it doesn't exist)
connection = sqlite3.connect('Greatest.db')

# Create a cursor object to execute SQL commands
cur = connection.cursor()

# Start the transaction
connection.execute('BEGIN TRANSACTION;')

try:
    # Step 1: Create the initial table with all necessary columns
    cur.execute('''
        CREATE TABLE IF NOT EXISTS "Constructor Data" (
            constructorId INTEGER,
            raceId INTEGER,
            constructorStandingsId INTEGER,
            name TEXT,
            nationality TEXT,
            standings_points INTEGER,
            wins INTEGER,
            circuit_name TEXT,
            location TEXT,
            country TEXT,
            year INTEGER
        )
    ''')

    # Step 2: Populate the table using JOIN
    cur.execute('''
        INSERT INTO "Constructor Data" (
            constructorId, 
            raceId, 
            constructorStandingsId, 
            name, 
            nationality, 
            standings_points, 
            wins, 
            circuit_name, 
            location, 
            country, 
            year
        )
        SELECT DISTINCT
            constructorStandings.constructorId,
            constructorStandings.raceId,
            constructorStandings.constructorStandingsId,
            Constructors.name,
            Constructors.nationality,
            constructorStandings.points AS standings_points,
            constructorStandings.wins,
            Circuits.name AS circuit_name,
            Circuits.location,
            Circuits.country,
            Races.year
        FROM "Constructor Standings" AS constructorStandings
        INNER JOIN Constructors ON constructorStandings.constructorId = Constructors.constructorId
        INNER JOIN Races ON constructorStandings.raceId = Races.raceId
        INNER JOIN Circuits ON Races.circuitId = Circuits.circuitId
    ''')

    # Commit the transaction
    connection.commit()

except Exception as error:
    connection.rollback()
    print("Transaction failed. Check database in 'DB Browser for SQLite.'\n", error)

finally:
    cur.close()
    connection.close()
