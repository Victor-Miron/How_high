import sqlite3

# Connect to sql database or create one if table doesn't exist
conn = sqlite3.connect('Greatest.db')

# Create a cursor object to execute SQL commands
cur = conn.cursor()

# Wrap the operations in a single transaction
conn.execute('BEGIN TRANSACTION;')
try:
    # Create a temporary table for constructor standings
    cur.execute('''
        CREATE TEMPORARY TABLE TempConstructorStandings AS
        SELECT constructorId, points AS standings_points, position, wins
        FROM "Constructor standings"
    ''')

    # Create temporary table for constructor results
    cur.execute('''
        CREATE TEMPORARY TABLE TempConstructorResults AS
        SELECT constructorID, points AS results_points
        FROM "Constructor results"
    ''')

    # Create the main table using SELECT
    cur.execute('''
        CREATE TABLE IF NOT EXISTS "Constructor Data" AS
        SELECT "Constructors".name, "Constructors".nationality,
            "TempConstructorStandings".standings_points, "TempConstructorStandings".position, 
            "TempConstructorStandings".wins,
            "TempConstructorResults".results_points,
            "Results".number, "Results".grid, "Results".position,
            "Circuits".name AS circuit_name, "Circuits".location, "Circuits".country,
            "Races".name AS race_name, "Races".date, Seasons.year
        FROM Constructors
        INNER JOIN "TempConstructorStandings" ON "TempConstructorStandings".constructorID=Constructors.constructorID
        INNER JOIN "TempConstructorResults" ON "TempConstructorResults".constructorID=Constructors.constructorID
        INNER JOIN "Results" ON Results.constructorID=Constructors.constructorID
        INNER JOIN "Seasons" ON Seasons.year=Races.year
        INNER JOIN "Circuits" ON Circuits.circuitID=Races.circuitID
        INNER JOIN "Races" ON Races.raceID=Results.raceID;
    ''')

    # Commit the transaction
    conn.commit()
except Exception as e:
    conn.rollback()
    print(f"Transaction failed: {e}")
finally:
    cur.close()
    conn.close()
