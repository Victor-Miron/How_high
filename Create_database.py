import pandas as pd
import sqlite3

# Connect to sql database or create one if table doesn't exist
conn = sqlite3.connect('Greatest.db')

# Create a cursor object to execute SQL commands
cur = conn.cursor()

# Use transaction for better performance
conn.execute('BEGIN TRANSACTION;')
try:
    # Read the CSV file into a DataFrame
    circuits_df = pd.read_csv('archive/circuits.csv')

    # Create table Circuits
    cur.execute('''
        CREATE TABLE IF NOT EXISTS Circuits (
        circuitId INTEGER,
        circuitRef TEXT,
        name TEXT,
        location TEXT,
        country TEXT,
        lat REAL,
        lng REAL,
        alt REAL,
        url TEXT
        )
    ''')
    # Convert DataFrame to list of tuples
    circuits_df = [tuple(row) for row in circuits_df.to_numpy()]
    # Insert Data into the table

    cur.executemany('''
        INSERT INTO Circuits (circuitId, circuitRef, name, location, country, lat, lng, alt, url)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', circuits_df)

    constructor_results_df = pd.read_csv('archive/constructor_results.csv')
    # Create table Constructor_results
    cur.execute('''
        CREATE TABLE IF NOT EXISTS 'Constructor results' (
            constructorResultsId INTEGER,
            raceId INTEGER,
            constructorId INTEGER,
            points INTEGER,
            status TEXT
        )
    ''')

    # Convert DataFrame to list of tuples
    constructor_results_df = [tuple(row) for row in constructor_results_df.to_numpy()]

    cur.executemany('''
        INSERT INTO 'Constructor results' (constructorResultsId, raceId, constructorId, points, status)
        VALUES (?, ?, ?, ?, ?)
    ''', constructor_results_df)

    # Read the CSV file into a DataFrame
    constructor_standings_df = pd.read_csv('archive/constructor_standings.csv')
    # Create table Constructor_standings
    cur.execute('''
        CREATE TABLE IF NOT EXISTS 'Constructor standings' (
            constructorStandingsId INTEGER,
            raceId INTEGER,
            constructorId INTEGER,
            points INTEGER,
            position INTEGER,
            positionText TEXT,
            wins INTEGER
        )
    ''')
    # Convert DataFrame to list of tuples
    constructor_standings_df = [tuple(row) for row in constructor_standings_df.to_numpy()]

    cur.executemany('''
        INSERT INTO 'Constructor standings' (constructorStandingsId, raceId, constructorId, points,
        position, positionText, wins)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', constructor_standings_df)

    constructors_df = pd.read_csv('archive/constructors.csv')
    # Create table Constructors
    cur.execute('''
        CREATE TABLE IF NOT EXISTS Constructors (
            constructorId INTEGER,
            constructorRef TEXT,
            name TEXT,
            nationality TEXT,
            url TEXT
        )
    ''')
    # Convert DataFrame to list of tuples
    constructors_df = [tuple(row) for row in constructors_df.to_numpy()]

    cur.executemany('''
        INSERT INTO Constructors (constructorId, constructorRef, name, nationality, url)
        VALUES (?, ?, ?, ?, ?)
    ''', constructors_df)

    drivers_df = pd.read_csv('archive/drivers.csv')
    # Create table Drivers
    cur.execute('''
        CREATE TABLE IF NOT EXISTS Drivers (
           driverId INTEGER,
           driverRef TEXT,
           number INTEGER,
           code TEXT,
           forename TEXT,
           surname TEXT,
           dob TEXT,
           nationality TEXT,
           url TEXT
        )
    ''')
    # Convert DataFrame to list of tuples
    drivers_df = [tuple(row) for row in drivers_df.to_numpy()]

    cur.executemany('''
        INSERT INTO Drivers (driverId, driverRef, number, code, forename, surname, dob, nationality, url)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', drivers_df)

    lap_times_df = pd.read_csv('archive/lap_times.csv')
    # Create table Lap Times
    cur.execute('''
        CREATE TABLE IF NOT EXISTS 'Lap Times' (
          raceId INTEGER,
          driverId INTEGER,
          lap INTEGER,
          position INTEGER,
          time TEXT,
          milliseconds INTEGER
        )
    ''')
    # Convert DataFrame to list of tuples
    lap_times_df = [tuple(row) for row in lap_times_df.to_numpy()]

    cur.executemany('''
        INSERT INTO 'Lap Times' (raceId, driverId, lap, position, time, milliseconds)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', lap_times_df)

    pit_stops_df = pd.read_csv('archive/pit_stops.csv')
    # Create table Pit Stops
    cur.execute('''
        CREATE TABLE IF NOT EXISTS 'Pit Stops' (
        raceId INTEGER,
        driverId INTEGER,
        stop INTEGER,
        lap INTEGER,
        time TEXT,
        duration TEXT,
        milliseconds INTEGER
        )
    ''')

    # Convert DataFrame to list of tuples
    pit_stops_df = [tuple(row) for row in pit_stops_df.to_numpy()]
    cur.executemany('''
        INSERT INTO 'Pit Stops' (raceId, driverId, stop, lap, time, duration, milliseconds)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', pit_stops_df)

    qualifying_df = pd.read_csv('archive/qualifying.csv')
    # Create table Qualifying
    cur.execute('''
        CREATE TABLE IF NOT EXISTS 'Qualifying' (
        qualifyId INTEGER,
        raceId INTEGER,
        driverId INTEGER,
        constructorId INTEGER,
        number INTEGER,
        position INTEGER,
        q1 TEXT,
        q2 TEXT,
        q3 TEXT
        )
    ''')

    qualifying_df = [tuple(row) for row in qualifying_df.to_numpy()]
    cur.executemany('''
        INSERT INTO 'Qualifying' (qualifyId, raceId, driverId, constructorId, number, position, q1, q2, q3)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', qualifying_df)

    races_df = pd.read_csv('archive/races.csv')
    # Create table Races
    cur.execute('''
        CREATE TABLE IF NOT EXISTS 'Races' (
        raceId INTEGER,
        year INTEGER,
        round INTEGER,
        circuitId INTEGER,
        name TEXT,
        date TEXT,
        time TEXT,
        url TEXT,
        fp1_date TEXT,
        fp1_time TEXT,
        fp2_date TEXT,
        fp2_time TEXT,
        fp3_date TEXT,
        fp3_time TEXT,
        quali_date TEXT,
        quali_time TEXT,
        sprint_date TEXT,
        sprint_time TEXT
        )
    ''')

    races_df = [tuple(row) for row in races_df.to_numpy()]
    cur.executemany('''
        INSERT INTO 'Races' (raceId, year, round, circuitId, name, date, time, url,
        fp1_date, fp1_time, fp2_date, fp2_time, fp3_date, fp3_time, quali_date, quali_time, sprint_date, sprint_time)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', races_df)

    results_df = pd.read_csv('archive/results.csv')

    # Create table Results
    cur.execute('''
        CREATE TABLE IF NOT EXISTS 'Results' (
        resultId INTEGER,
        raceId INTEGER,
        driverId INTEGER,
        constructorId INTEGER,
        number INTEGER,
        grid INTEGER,
        position INTEGER,
        positionText TEXT,
        positionOrder INTEGER,
        points INTEGER,
        laps INTEGER,
        time TEXT,
        milliseconds INTEGER,
        fastestLap INTEGER,
        rank INTEGER,
        fastestLapTime TEXT,
        fastestLapSpeed TEXT,
        statusId INTEGER
        )
    ''')

    results_df = [tuple(row) for row in results_df.to_numpy()]

    cur.executemany('''
        INSERT INTO 'Results' (resultId, raceId, driverId, constructorId, 
        number, grid, position, positionText, positionOrder, points, laps, time, 
        milliseconds, fastestLap, rank, fastestLapTime, fastestLapSpeed, statusId)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', results_df)

    seasons_df = pd.read_csv('archive/seasons.csv')
    # Create table Seasons
    cur.execute('''
        CREATE TABLE IF NOT EXISTS 'Seasons' (
        year INTEGER,
        url TEXT
        )
    ''')

    seasons_df = [tuple(row) for row in seasons_df.to_numpy()]
    cur.executemany('''
        INSERT INTO 'Seasons' (year, url)
        VALUES (?, ?)
    ''', seasons_df)

    sprint_results_df = pd.read_csv('archive/sprint_results.csv')

    # Create table Sprint Results
    cur.execute('''
        CREATE TABLE IF NOT EXISTS 'Sprint Results' (
            resultId INTEGER,
            raceId INTEGER,
            driverId INTEGER,
            constructorId INTEGER,
            number INTEGER,
            grid INTEGER,
            position INTEGER,
            positionText TEXT,
            positionOrder INTEGER,
            points INTEGER,
            laps INTEGER,
            time INTEGER,
            milliseconds INTEGER,
            fastestLap INTEGER,
            fastestLapTime TEXT,
            statusId INTEGER
        )
    ''')

    sprint_results_df = [tuple(row) for row in sprint_results_df.to_numpy()]
    cur.executemany('''
        INSERT INTO 'Sprint Results' (resultId, raceId, driverId, constructorId, number, 
        grid, position, positionText, positionOrder, points, laps, time,
         milliseconds, fastestLap, fastestLapTime, statusId)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', sprint_results_df)

    status_df = pd.read_csv('archive/status.csv')
    # Create table Status
    cur.execute('''
        CREATE TABLE IF NOT EXISTS 'Status' (
        statusId INTEGER,
        status TEXT
        )
    ''')
    status_df = [tuple(row) for row in status_df.to_numpy()]

    cur.executemany('''
        INSERT INTO 'Status' (statusId, status)
        VALUES (?, ?)
    ''', status_df)

    # Commit transaction
    conn.commit()

except Exception as e:
    # Rollback transaction if any operation fails
    conn.rollback()
    print(f"Transaction failed: {e}")

finally:
    cur.close()
    conn.close()
