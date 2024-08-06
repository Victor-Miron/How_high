import sqlite3

# Connect to the SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('Greatest.db')

# Create a cursor object to execute SQL commands
cur = conn.cursor()

# Start the transaction
conn.execute('BEGIN TRANSACTION;')

try:
    # Step 1: Create the initial table with all necessary columns
    cur.execute('''
        CREATE TABLE IF NOT EXISTS "Drivers Data" (
            driverId INTEGER,
            raceId INTEGER,
            resultId INTEGER,
            Forename TEXT,
            Surname TEXT,
            Nationality TEXT,
            Year INTEGER,
            "Circuit Name" TEXT,
            Points INTEGER,
            Rank INTEGER,
            FastestLapTime TEXT
        )
    ''')

    # Step 2: Populate the table with data using JOIN
    cur.execute('''
        INSERT INTO "Drivers Data" (driverId, raceId, resultId, Forename, Surname, Nationality, Year, "Circuit Name", 
        Points, Rank, FastestLapTime)
        SELECT DISTINCT
            Results.driverId,
            Results.raceId,
            Results.resultId,
            Drivers.forename AS Forename,
            Drivers.surname AS Surname,
            Drivers.nationality AS Nationality,
            Races.year AS Year,
            Races.name AS "Circuit Name",
            Results.points AS Points,
            CASE 
                WHEN Results.rank = '\\N' THEN 0
                ELSE Results.rank
            END AS Rank,
            CASE 
                WHEN Results.fastestLapTime = '\\N' THEN '0'
                ELSE Results.fastestLapTime
            END AS FastestLapTime
        FROM Results
        INNER JOIN Drivers ON Results.driverId = Drivers.driverId
        INNER JOIN Races ON Results.raceId = Races.raceId
    ''')

    # Commit the transaction
    conn.commit()
except Exception as e:
    conn.rollback()
    print("Transaction failed. Check database in 'DB Browser for SQLite.'\n", e)
finally:
    cur.close()
    conn.close()
