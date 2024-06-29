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
            raceId INTEGER
        )
    ''')

    # Step 2: Populate the table with the primary keys
    cur.execute('''
        INSERT INTO "Constructor Data" (constructorId, raceId)
        SELECT DISTINCT constructorId, raceId
        FROM Results
    ''')

    # Step 3: Add columns from Constructors
    cur.execute('ALTER TABLE "Constructor Data" ADD COLUMN name TEXT')
    cur.execute('ALTER TABLE "Constructor Data" ADD COLUMN nationality TEXT')
    cur.execute('''
        UPDATE "Constructor Data"
        SET name = (SELECT name FROM Constructors WHERE Constructors.constructorId = "Constructor Data".constructorId),
            nationality = (SELECT nationality FROM Constructors WHERE Constructors.constructorId = "Constructor Data".constructorId)
    ''')

    # Step 4: Add columns from TempConstructorStandings
    cur.execute('ALTER TABLE "Constructor Data" ADD COLUMN standings_points INTEGER')
    cur.execute('ALTER TABLE "Constructor Data" ADD COLUMN standings_position INTEGER')
    cur.execute('ALTER TABLE "Constructor Data" ADD COLUMN wins INTEGER')
    cur.execute('''
        UPDATE "Constructor Data"
        SET standings_points = (SELECT points FROM "Constructor standings" WHERE "Constructor standings".constructorId = "Constructor Data".constructorId),
            standings_position = (SELECT position FROM "Constructor standings" WHERE "Constructor standings".constructorId = "Constructor Data".constructorId),
            wins = (SELECT wins FROM "Constructor standings" WHERE "Constructor standings".constructorId = "Constructor Data".constructorId)
    ''')

    # Step 5: Add columns from TempConstructorResults
    cur.execute('ALTER TABLE "Constructor Data" ADD COLUMN results_points INTEGER')
    cur.execute('''
        UPDATE "Constructor Data"
        SET results_points = (SELECT points FROM "Constructor results" WHERE "Constructor results".constructorId = "Constructor Data".constructorId)
    ''')

    # Step 6: Add columns from Results
    cur.execute('ALTER TABLE "Constructor Data" ADD COLUMN result_number INTEGER')
    cur.execute('ALTER TABLE "Constructor Data" ADD COLUMN grid INTEGER')
    cur.execute('ALTER TABLE "Constructor Data" ADD COLUMN result_position INTEGER')
    cur.execute('''
        UPDATE "Constructor Data"
        SET result_number = (SELECT number FROM Results WHERE Results.constructorId = "Constructor Data".constructorId AND Results.raceId = "Constructor Data".raceId),
            grid = (SELECT grid FROM Results WHERE Results.constructorId = "Constructor Data".constructorId AND Results.raceId = "Constructor Data".raceId),
            result_position = (SELECT position FROM Results WHERE Results.constructorId = "Constructor Data".constructorId AND Results.raceId = "Constructor Data".raceId)
    ''')

    # Step 7: Add columns from Circuits
    cur.execute('ALTER TABLE "Constructor Data" ADD COLUMN circuit_name TEXT')
    cur.execute('ALTER TABLE "Constructor Data" ADD COLUMN location TEXT')
    cur.execute('ALTER TABLE "Constructor Data" ADD COLUMN country TEXT')
    cur.execute('''
        UPDATE "Constructor Data"
        SET circuit_name = (SELECT name FROM Circuits WHERE Circuits.circuitId = (SELECT circuitId FROM Races WHERE Races.raceId = "Constructor Data".raceId)),
            location = (SELECT location FROM Circuits WHERE Circuits.circuitId = (SELECT circuitId FROM Races WHERE Races.raceId = "Constructor Data".raceId)),
            country = (SELECT country FROM Circuits WHERE Circuits.circuitId = (SELECT circuitId FROM Races WHERE Races.raceId = "Constructor Data".raceId))
    ''')

    # Step 8: Add columns from Races
    cur.execute('ALTER TABLE "Constructor Data" ADD COLUMN race_name TEXT')
    cur.execute('ALTER TABLE "Constructor Data" ADD COLUMN race_date TEXT')
    cur.execute('''
        UPDATE "Constructor Data"
        SET race_name = (SELECT name FROM Races WHERE Races.raceId = "Constructor Data".raceId),
            race_date = (SELECT date FROM Races WHERE Races.raceId = "Constructor Data".raceId)
    ''')

    # Step 9: Add columns from Seasons
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
