import sqlite3

# Connect to the SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('Greatest.db')

# Create a cursor object to execute SQL commands
cur = conn.cursor()

# Start the transaction
conn.execute('BEGIN TRANSACTION;')

try:
    # Step 1: Create the initial table with the primary keys
    cur.execute('''
        CREATE TABLE IF NOT EXISTS "Constructor Data" (
            constructorId INTEGER,
            raceId INTEGER,
            constructorStandingsId INTEGER
        )
    ''')

    # Step 2: Populate the table with the primary keys
    cur.execute('''
        INSERT INTO "Constructor Data" (constructorId, raceId, constructorStandingsId)
        SELECT DISTINCT constructorId, raceId, constructorStandingsId
        FROM "Constructor Standings"
    ''')

    # Step 3: Add columns from Constructors
    cur.execute('ALTER TABLE "Constructor Data" ADD COLUMN name TEXT')
    cur.execute('ALTER TABLE "Constructor Data" ADD COLUMN nationality TEXT')
    cur.execute('''
        UPDATE "Constructor Data"
        SET name = (SELECT name FROM Constructors 
                WHERE Constructors.constructorId = "Constructor Data".constructorId),
            nationality = (SELECT nationality FROM Constructors 
                WHERE Constructors.constructorId = "Constructor Data".constructorId)
    ''')

    # Step 4: Add columns from TempConstructorStandings
    cur.execute('ALTER TABLE "Constructor Data" ADD COLUMN standings_points INTEGER')
    cur.execute('ALTER TABLE "Constructor Data" ADD COLUMN wins INTEGER')
    cur.execute('''
        UPDATE "Constructor Data"
        SET standings_points = (SELECT points FROM "Constructor standings" 
                WHERE "Constructor standings".constructorStandingsId = "Constructor Data".constructorStandingsId),
            wins = (SELECT wins FROM "Constructor standings" 
                WHERE "Constructor standings".raceId = "Constructor Data".raceId)
    ''')

    # Step 5: Add columns from Circuits
    cur.execute('ALTER TABLE "Constructor Data" ADD COLUMN circuit_name TEXT')
    cur.execute('ALTER TABLE "Constructor Data" ADD COLUMN location TEXT')
    cur.execute('ALTER TABLE "Constructor Data" ADD COLUMN country TEXT')
    cur.execute('''
        UPDATE "Constructor Data"
        SET circuit_name = (SELECT name FROM Circuits 
                WHERE Circuits.circuitId = (SELECT circuitId FROM Races 
                    WHERE Races.raceId = "Constructor Data".raceId)),
            location = (SELECT location FROM Circuits 
                WHERE Circuits.circuitId = (SELECT circuitId FROM Races 
                    WHERE Races.raceId = "Constructor Data".raceId)),
            country = (SELECT country FROM Circuits 
                WHERE Circuits.circuitId = (SELECT circuitId FROM Races 
                    WHERE Races.raceId = "Constructor Data".raceId))
    ''')

    # Step 6: Add columns from Seasons
    cur.execute('ALTER TABLE "Constructor Data" ADD COLUMN year INTEGER')
    cur.execute('''
    UPDATE "Constructor Data"
    SET year = (SELECT year FROM Races WHERE Races.raceId = "Constructor Data".raceId)
''')

    # Commit the transaction
    conn.commit()
except Exception as e:
    conn.rollback()
    print(f"Transaction failed: {e}")
finally:
    cur.close()
    conn.close()
