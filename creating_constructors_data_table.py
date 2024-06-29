# # Select columns from different tables and create the tabla Constructor Data
#
# cur.execute('''
#     CREATE TABLE IF NOT EXISTS "Constructor Data" AS
#         SELECT "Constructors".name, "Constructors".nationality,
#         "Constructor standings".points, "Constructor Standings".position, "Constructor Standings".wins,
#         "Constructor results".points,
#         "Results".number, "Results".grid, "Results".position,
#         "Circuits".name, "Circuits".location, "Circuits".country,
#         "Races".name, "Races".date,
#         "Seasons".year
#         FROM Constructors
#         INNER JOIN "Constructor Standings" ON "Constructor Standings".constructorID=Constructors.constructorID
#         INNER JOIN "Constructor results" ON "Constructor results".constructorID=Constructors.constructorID
#         INNER JOIN "Results" ON Results.constructorID=Constructors.constructorID
#         INNER JOIN "Seasons" ON Seasons.year=Races.year
#         INNER JOIN "Circuits" ON Circuits.circuitID=Races.circuitID
#         INNER JOIN "Races" ON Races.raceID=Results.raceID;
#         ''')
#
# conn.commit()
# cur.close()
# conn.close()

import pandas as pd
import sqlite3

# Connect to sql database or create one if table doesn't exist
conn = sqlite3.connect('Greatest.db')

# Create a cursor object to execute SQL commands
cur = conn.cursor()

# Use transaction for better performance
conn.execute('BEGIN TRANSACTION;')

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

# Insert Data into the table
cur.executemany('''
    INSERT INTO Circuits (circuitId, circuitRef, name, location, country, lat, lng, alt, url)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
''', circuits_df.values.tolist())

# Repeat the same process for the remaining tables
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

constructor_results_df = pd.read_csv('/mnt/data/archive/constructor_results.csv')
cur.executemany('''
    INSERT INTO 'Constructor results' (constructorResultsId, raceId, constructorId, points, status)
    VALUES (?, ?, ?, ?, ?)
''', constructor_results_df.values.tolist())

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

constructor_standings_df = pd.read_csv('/mnt/data/archive/constructor_standings.csv')
cur.executemany('''
    INSERT INTO 'Constructor standings' (constructorStandingsId, raceId, constructorId, points, position, positionText, wins)
    VALUES (?, ?, ?, ?, ?, ?, ?)
''', constructor_standings_df.values.tolist())

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

constructors_df = pd.read_csv('/mnt/data/archive/constructors.csv')
cur.executemany('''
    INSERT INTO Constructors (constructorId, constructorRef, name, nationality, url)
    VALUES (?, ?, ?, ?, ?)
''', constructors_df.values.tolist())

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

drivers_df = pd.read_csv('/mnt/data/archive/drivers.csv')
cur.executemany('''
    INSERT INTO Drivers (driverId, driverRef, number, code, forename, surname, dob, nationality, url)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
''', drivers_df.values.tolist())

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

lap_times_df = pd.read_csv('/mnt/data/archive/lap_times.csv')
cur.executemany('''
    INSERT INTO 'Lap Times' (raceId, driverId, lap, position, time, milliseconds)
    VALUES (?, ?, ?, ?, ?, ?)
''', lap_times_df.values.tolist())

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

pit_stops_df = pd.read_csv('/mnt/data/archive/pit_stops.csv')
cur.executemany('''
    INSERT INTO 'Pit Stops' (raceId, driverId, stop, lap, time, duration, milliseconds)
    VALUES (?, ?, ?, ?, ?, ?, ?)
''', pit_stops_df.values.tolist())

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

qualifying_df = pd.read_csv('/mnt/data/archive/qualifying.csv')
cur.executemany('''
    INSERT INTO 'Qualifying' (qualifyId, raceId, driverId, constructorId, number, position, q1, q2, q3)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
''', qualifying_df.values.tolist())

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

races_df = pd.read_csv('/mnt/data/archive/races.csv')
cur.executemany('''
    INSERT INTO 'Races' (raceId, year, round, circuitId, name, date, time, url, fp1_date, fp1_time, fp2_date, fp2_time, fp3_date, fp3_time, quali_date, quali_time, sprint_date, sprint_time)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
''', races_df.values.tolist())

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

results_df = pd.read_csv('/mnt/data/archive/results.csv')
cur.executemany('''
    INSERT INTO 'Results' (resultId, raceId, driverId, constructorId, number, grid, position, positionText, positionOrder, points, laps, time, milliseconds, fastestLap, rank, fastestLapTime, fastestLapSpeed, statusId)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
''', results_df.values.tolist())

# Create table Seasons
cur.execute('''
    CREATE TABLE IF NOT EXISTS 'Seasons' (
    year INTEGER,
    url TEXT
    )
''')

seasons_df = pd.read_csv('/mnt/data/archive/seasons.csv')
cur.executemany('''
    INSERT INTO 'Seasons' (year, url)
    VALUES (?, ?)
''', seasons_df.values.tolist())

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

sprint_results_df = pd.read_csv('/mnt/data/archive/sprint_results.csv')
cur.executemany('''
    INSERT INTO 'Sprint Results' (resultId, raceId, driverId, constructorId, number, grid, position, positionText, positionOrder, points, laps, time, milliseconds, fastestLap, fastestLapTime, statusId)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
''', sprint_results_df.values.tolist())

# Create table Status
cur.execute('''
    CREATE TABLE IF NOT EXISTS 'Status' (
    statusId INTEGER,
    status TEXT
    )
''')

status_df = pd.read_csv('/mnt/data/archive/status.csv')
cur.executemany('''
    INSERT INTO 'Status' (statusId, status)
    VALUES (?, ?)
''', status_df.values.tolist())

# Commit transaction
conn.commit()

cur.close()
conn.close()
