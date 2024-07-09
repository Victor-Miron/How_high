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
        CREATE TABLE IF NOT EXISTS "Drivers Data" (
            driverId INTEGER,
            raceId INTEGER,
            resultId Integer
        )
    ''')

    # Step 2: Populate the table with the primary keys
    cur.execute('''
        INSERT INTO "Drivers Data" (driverId, raceId, resultId)
        SELECT DISTINCT driverId, raceId, resultId
        FROM "Results"
    ''')

    # Step 3: Add columns from Drivers
    cur.execute('ALTER TABLE "Drivers Data" ADD COLUMN Forename TEXT')
    cur.execute('ALTER TABLE "Drivers Data" ADD COLUMN Surname TEXT')
    cur.execute('ALTER TABLE "Drivers Data" ADD COLUMN Nationality TEXT')
    cur.execute('''
        UPDATE "Drivers Data"
        SET Forename = (SELECT forename FROM Drivers
                WHERE Drivers.driverId = "Drivers Data".driverId),
            Surname = (SELECT surname FROM Drivers
                WHERE Drivers.driverId = "Drivers Data".driverId),
            Nationality = (SELECT nationality FROM Drivers 
                WHERE Drivers.driverId = "Drivers Data".driverId)
    ''')

    # Step 4: Add columns from TempRaces
    cur.execute('ALTER TABLE "Drivers Data" ADD COLUMN Year INTEGER')
    cur.execute('ALTER TABLE "Drivers Data" ADD COLUMN "Circuit Name" INTEGER')
    cur.execute('ALTER TABLE "Drivers Data" ADD COLUMN Position INTEGER')
    cur.execute('''
        UPDATE "Drivers Data"
        SET Year = (SELECT year FROM "Races" 
                WHERE Races.raceId = "Drivers Data".raceId),
            "Circuit name" = (SELECT name FROM "Races" 
                WHERE Races.raceId = "Drivers Data".raceId),
            Position = (SELECT position FROM Results 
                WHERE Results.resultId = "Drivers Data".resultId)
    ''')

    # Commit the transaction
    conn.commit()
except Exception as e:
    conn.rollback()
    print(f"Transaction failed: {e}")
finally:
    cur.close()
    conn.close()
