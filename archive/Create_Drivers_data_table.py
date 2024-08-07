import sqlite3

# Connect to the SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('../Greatest.db')

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

    # Step 4: Add columns from TempResults
    cur.execute('ALTER TABLE "Drivers Data" ADD COLUMN Year INTEGER')
    cur.execute('ALTER TABLE "Drivers Data" ADD COLUMN "Circuit Name" TEXT')
    cur.execute('ALTER TABLE "Drivers Data" ADD COLUMN Points INTEGER')
    cur.execute('ALTER TABLE "Drivers Data" ADD COLUMN Rank INTEGER')
    cur.execute('ALTER TABLE "Drivers Data" ADD COLUMN FastestLapTime TEXT')
    cur.execute('''
        UPDATE "Drivers Data"
        SET Year = (SELECT year FROM "Races" 
                WHERE Races.raceId = "Drivers Data".raceId),
            "Circuit Name" = (SELECT name FROM "Races" 
                WHERE Races.raceId = "Drivers Data".raceId), 
            Points = (SELECT points FROM Results 
                WHERE Results.resultId = "Drivers Data".resultId),
            Rank= (SELECT rank FROM Results 
                WHERE Results.resultId = "Drivers Data".resultId),
            FastestLapTime = (SELECT fastestLapTime FROM Results 
                WHERE Results.resultId = "Drivers Data".resultId)
    ''')
    cur.execute('''
        UPDATE "Drivers Data"
        SET 
        Rank = REPLACE(Rank, '\\N', 0),
        FastestLapTime = REPLACE(FastestLapTime, '\\N', 0)
        WHERE Rank LIKE '%\\N%' OR FastestLapTime LIKE '%\\N%';
''')
    # Commit the transaction
    conn.commit()
except Exception as e:
    conn.rollback()
    print("Transaction already exists. Check database in 'DB Browser for SQLite.'\n", {e})
finally:
    cur.close()
    conn.close()
