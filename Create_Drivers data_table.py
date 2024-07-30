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
        CREATE TABLE IF NOT EXISTS Drivers_Data (
            driverId INTEGER,
            raceId INTEGER,
            resultId INTEGER
        )
    ''')

    # Step 2: Populate the table with the primary keys
    cur.execute('''
        INSERT INTO Drivers_Data (driverId, raceId, resultId)
        SELECT DISTINCT driverId, raceId, resultId
        FROM Results
    ''')

    # Step 3: Add columns from Drivers
    cur.execute('ALTER TABLE Drivers_Data ADD COLUMN Forename TEXT')
    cur.execute('ALTER TABLE Drivers_Data ADD COLUMN Surname TEXT')
    cur.execute('ALTER TABLE Drivers_Data ADD COLUMN Nationality TEXT')
    cur.execute('''
        UPDATE Drivers_Data
        SET Forename = (SELECT forename FROM Drivers
                WHERE Drivers.driverId = Drivers_Data.driverId),
            Surname = (SELECT surname FROM Drivers
                WHERE Drivers.driverId = Drivers_Data.driverId),
            Nationality = (SELECT nationality FROM Drivers 
                WHERE Drivers.driverId = Drivers_Data.driverId)
    ''')

    # Step 4: Add columns from Results and Races
    cur.execute('ALTER TABLE Drivers_Data ADD COLUMN Year INTEGER')
    cur.execute('ALTER TABLE Drivers_Data ADD COLUMN Circuit_Name TEXT')
    cur.execute('ALTER TABLE Drivers_Data ADD COLUMN Points INTEGER')
    cur.execute('ALTER TABLE Drivers_Data ADD COLUMN Time TEXT')
    cur.execute('ALTER TABLE Drivers_Data ADD COLUMN Rank INTEGER')
    cur.execute('ALTER TABLE Drivers_Data ADD COLUMN FastestLapTime TEXT')
    cur.execute('''
        UPDATE Drivers_Data
        SET Year = (SELECT year FROM Races 
                WHERE Races.raceId = Drivers_Data.raceId),
            Circuit_Name = (SELECT name FROM Circuits
                WHERE Circuits.circuitId = (SELECT circuitId FROM Races WHERE Races.raceId = Drivers_Data.raceId)), 
            Points = (SELECT points FROM Results 
                WHERE Results.resultId = Drivers_Data.resultId),
            Time = (SELECT time FROM Results 
                WHERE Results.resultId = Drivers_Data.resultId),
            Rank= (SELECT rank FROM Results 
                WHERE Results.resultId = Drivers_Data.resultId),
            FastestLapTime = (SELECT fastestLapTime FROM Results 
                WHERE Results.resultId = Drivers_Data.resultId)
    ''')

    # Commit the transaction
    conn.commit()
except Exception as e:
    conn.rollback()
    print(f"Transaction failed: {e}")
finally:
    cur.close()
    conn.close()
