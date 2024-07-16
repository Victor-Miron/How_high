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

    # Select only the columns needed
    circuits_df = circuits_df[['circuitId', 'circuitRef', 'name', 'location', 'country']]

    # Create table Circuits
    cur.execute('''
        CREATE TABLE IF NOT EXISTS Circuits (
        circuitId INTEGER,
        circuitRef TEXT,
        name TEXT,
        location TEXT,
        country TEXT
        )
    ''')
    # Convert DataFrame to list of tuples
    circuits_df = [tuple(row) for row in circuits_df.to_numpy()]
    # Insert Data into the table

    cur.executemany('''
        INSERT INTO Circuits (circuitId, circuitRef, name, location, country)
        VALUES (?, ?, ?, ?, ?)
    ''', circuits_df)

    constructor_results_df = pd.read_csv('archive/constructor_results.csv')
    # Select only the columns needed
    constructor_results_df = constructor_results_df[['constructorResultsId', 'raceId', 'constructorId', 'points']]

    # Create table Constructor_results
    cur.execute('''
        CREATE TABLE IF NOT EXISTS 'Constructor results' (
            constructorResultsId INTEGER,
            raceId INTEGER,
            constructorId INTEGER,
            points INTEGER
        )
    ''')

    # Convert DataFrame to list of tuples
    constructor_results_df = [tuple(row) for row in constructor_results_df.to_numpy()]

    cur.executemany('''
        INSERT INTO 'Constructor results' (constructorResultsId, raceId, constructorId, points)
        VALUES (?, ?, ?, ?)
    ''', constructor_results_df)

    # Read the CSV file into a DataFrame
    constructor_standings_df = pd.read_csv('archive/constructor_standings.csv')
    # Select only the columns needed
    constructor_standings_df = constructor_standings_df[['constructorStandingsId', 'raceId', 'constructorId', 'points',
                                                         'position', 'wins']]

    # Create table Constructor_standings
    cur.execute('''
        CREATE TABLE IF NOT EXISTS 'Constructor standings' (
            constructorStandingsId INTEGER,
            raceId INTEGER,
            constructorId INTEGER,
            points INTEGER,
            position INTEGER,
            wins INTEGER
        )
    ''')
    # Convert DataFrame to list of tuples
    constructor_standings_df = [tuple(row) for row in constructor_standings_df.to_numpy()]

    cur.executemany('''
        INSERT INTO 'Constructor standings' (constructorStandingsId, raceId, constructorId, points,
        position, wins)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', constructor_standings_df)

    constructors_df = pd.read_csv('archive/constructors.csv')
    # Select only the columns needed
    constructors_df = constructors_df[['constructorId', 'constructorRef', 'name', 'nationality']]
    # Create table Constructors
    cur.execute('''
        CREATE TABLE IF NOT EXISTS Constructors (
            constructorId INTEGER,
            constructorRef TEXT,
            name TEXT,
            nationality TEXT
        )
    ''')
    # Convert DataFrame to list of tuples
    constructors_df = [tuple(row) for row in constructors_df.to_numpy()]

    cur.executemany('''
        INSERT INTO Constructors (constructorId, constructorRef, name, nationality)
        VALUES (?, ?, ?, ?)
    ''', constructors_df)

    drivers_df = pd.read_csv('archive/drivers.csv')
    # Select only the columns needed
    drivers_df = drivers_df[['driverId', 'driverRef', 'number', 'code', 'forename', 'surname', 'dob', 'nationality']]
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
           nationality TEXT
        )
    ''')
    # Convert DataFrame to list of tuples
    drivers_df = [tuple(row) for row in drivers_df.to_numpy()]

    cur.executemany('''
        INSERT INTO Drivers (driverId, driverRef, number, code, forename, surname, dob, nationality)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''', drivers_df)

    pit_stops_df = pd.read_csv('archive/pit_stops.csv')
    # Select only the columns needed
    pit_stops_df = pit_stops_df[['raceId', 'driverId', 'stop', 'lap', 'time', 'duration', 'milliseconds']]
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

    races_df = pd.read_csv('archive/races.csv')
    # Select only the columns needed
    races_df = races_df[['raceId', 'year', 'round', 'circuitId', 'name', 'date']]
    # Create table Races
    cur.execute('''
        CREATE TABLE IF NOT EXISTS 'Races' (
        raceId INTEGER,
        year INTEGER,
        round INTEGER,
        circuitId INTEGER,
        name TEXT,
        date TEXT
        )
    ''')

    races_df = [tuple(row) for row in races_df.to_numpy()]
    cur.executemany('''
        INSERT INTO 'Races' (raceId, year, round, circuitId, name, date)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', races_df)

    results_df = pd.read_csv('archive/results.csv')
    # Select only the columns needed
    results_df = results_df[['resultId', 'raceId', 'driverId', 'constructorId',
                             'number', 'points', 'time', 'rank', 'fastestLapTime']]
    # Create table Results
    cur.execute('''
        CREATE TABLE IF NOT EXISTS 'Results' (
        resultId INTEGER,
        raceId INTEGER,
        driverId INTEGER,
        constructorId INTEGER,
        number INTEGER,
        points INTEGER,
        time TEXT,
        rank INTEGER,
        fastestLapTime TEXT
        )
    ''')

    results_df = [tuple(row) for row in results_df.to_numpy()]

    cur.executemany('''
        INSERT INTO 'Results' (resultId, raceId, driverId, constructorId, 
        number, points, time, rank, fastestLapTime)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', results_df)

    seasons_df = pd.read_csv('archive/seasons.csv')
    seasons_df = seasons_df[['year']]
    # Create table Seasons
    cur.execute('''
        CREATE TABLE IF NOT EXISTS 'Seasons' (
        year INTEGER
        )
    ''')

    seasons_df = [tuple(row) for row in seasons_df.to_numpy()]
    cur.executemany('''
        INSERT INTO 'Seasons' (year)
        VALUES (?)
    ''', seasons_df)

    # Commit transaction
    conn.commit()

except Exception as e:
    # Rollback transaction if any operation fails
    conn.rollback()
    print(f"Transaction failed: {e}")

finally:
    cur.close()
    conn.close()
