import pandas as pd
import sqlite3

# Connect to sql database or create one if table doesn't exist
conn = sqlite3.connect('Greatest.db')

# Create a cursor object to execute SQL commands
cur = conn.cursor()

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


# Read the CSV file into a DataFrame
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

# Insert Data into the table
for index, row in constructor_results_df.iterrows():
    cur.execute('''
        INSERT INTO 'Constructor results' (constructorResultsId, raceId, constructorId, points, status)
        VALUES(?, ?, ?, ?, ?)
        ''', (row['constructorResultsId'], row['raceId'], row['constructorId'], row['points'], row['status']))

# Read the CSV file into a DataFrame
constructor_standings_df = pd.read_csv('archive/constructor_standings.csv')

# Create table constructor_standings
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


# Insert Data into the table
for index, row in constructor_standings_df.iterrows():
    cur.execute('''
        INSERT INTO 'Constructor standings' (constructorStandingsId,raceId,constructorId,
        points,position,positionText,wins)
        VALUES(?, ?, ?, ?, ?, ?, ?)
        ''', (row['constructorStandingsId'], row['raceId'], row['constructorId'], row['points'], row['position'],
              row['positionText'], row['wins']))

# Read the CSV file into a DataFrame
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


# Insert Data into the table
for index, row in constructors_df.iterrows():
    cur.execute('''
        INSERT INTO Constructors  (constructorId, constructorRef, name, nationality, url)
        VALUES(?, ?, ?, ?, ?)
        ''', (row['constructorId'], row['constructorRef'], row['name'], row['nationality'], row['url']))

# Read the CSV file into a DataFrame
drivers_df = pd.read_csv('archive/drivers.csv')

# Create table constructors
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


# Insert Data into the table
for index, row in drivers_df.iterrows():
    cur.execute('''
        INSERT INTO Drivers (driverId, driverRef, number, code, forename, surname, dob, nationality, url)
        VALUES(?, ?, ?, ?, ?, ? , ? ,? , ?)
        ''', (row['driverId'], row['driverRef'], row['number'], row['code'], row['forename'], row['surname'],
              row['dob'], row['nationality'], row['url']))

# Read the CSV file into a DataFrame
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


# Insert Data into the table
for index, row in lap_times_df.iterrows():
    cur.execute('''
        INSERT INTO 'Lap Times' (raceId,driverId,lap,position,time,milliseconds)
        VALUES(?, ?, ?, ?, ?, ?)
        ''', (row['raceId'], row['driverId'], row['lap'], row['position'], row['time'], row['milliseconds']))

# Read the CSV file into a DataFrame
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


# Insert Data into the table
for index, row in pit_stops_df.iterrows():
    cur.execute('''
        INSERT INTO 'Pit Stops' (raceId, driverId, stop,lap, time, duration, milliseconds)
        VALUES(?, ?, ?, ?, ?, ?, ?)
        ''', (row['raceId'], row['driverId'], row['stop'], row['lap'], row['time'],
              row['duration'], row['milliseconds']))

# Read the CSV file into a DataFrame
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


# Insert Data into the table
for index, row in qualifying_df.iterrows():
    cur.execute('''
        INSERT INTO 'Qualifying' (qualifyId, raceId, driverId, constructorId, number,
         position, q1, q2, q3)
        VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (row['qualifyId'], row['raceId'], row['driverId'], row['constructorId'], row['number'],
              row['position'], row['q1'], row['q2'], row['q3']))

# Read the CSV file into a DataFrame
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

# Insert Data into the table
for index, row in races_df.iterrows():
    cur.execute('''
        INSERT INTO 'Races' (raceId,year,round,circuitId,name,date,time,url,
        fp1_date,fp1_time,fp2_date,fp2_time,fp3_date,fp3_time,
        quali_date,quali_time,sprint_date,sprint_time)

        VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (row['raceId'], row['year'], row['round'], row['circuitId'], row['name'],
              row['date'], row['time'], row['url'], row['fp1_date'], row['fp1_time'], row['fp2_date'],
              row['fp2_time'], row['fp3_date'], row['fp3_time'],
              row['quali_date'], row['quali_time'], row['sprint_date'], row['sprint_time']))

# Read the CSV file into a DataFrame
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

# Insert Data into the table
for index, row in results_df.iterrows():
    cur.execute('''
        INSERT INTO 'Results' (resultId, raceId, driverId, constructorId, number,
        grid, position, positionText, positionOrder, points, laps, time, milliseconds,
        fastestLap, rank, fastestLapTime, fastestLapSpeed, statusId
)

        VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (row['resultId'], row['raceId'], row['driverId'], row['constructorId'], row['number'],
              row['grid'], row['position'], row['positionText'], row['positionOrder'], row['points'],
              row['laps'], row['time'], row['milliseconds'], row['fastestLap'],
              row['rank'], row['fastestLapTime'], row['fastestLapSpeed'], row['statusId']))

# Read the CSV file into a DataFrame
seasons_df = pd.read_csv('archive/seasons.csv')

# Create table Seasons
cur.execute('''
    CREATE TABLE IF NOT EXISTS 'Seasons' (
    year Integer,
    url TEXT
    )
''')


# Insert Data into the table
for index, row in seasons_df.iterrows():
    cur.execute('''
        INSERT INTO 'Seasons' (year, url)
        VALUES(?, ?)
        ''', (row['year'], row['url']))

# Read the CSV file into a DataFrame
seasons_df = pd.read_csv('archive/seasons.csv')

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

# Insert Data into the table
for index, row in results_df.iterrows():
    cur.execute('''
        INSERT INTO 'Results' (resultId, raceId, driverId, constructorId, number, grid, position,
        positionText, positionOrder, points, laps, time, milliseconds, fastestLap, fastestLapTime, statusId
)
        VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (row['resultId'], row['raceId'], row['driverId'], row['constructorId'],
              row['number'], row['grid'], row['position'], row['positionText'], row['positionOrder'],
              row['points'], row['laps'], row['time'], row['milliseconds'], row['fastestLap'],
              row['fastestLapTime'], row['statusId']))

# Read the CSV file into a DataFrame
status_df = pd.read_csv('archive/status.csv')

# Create table Status
cur.execute('''
    CREATE TABLE IF NOT EXISTS 'Status' (
    statusId INTEGER,
    status TEXT
    )
''')


# Insert Data into the table
for index, row in status_df.iterrows():
    cur.execute('''
        INSERT INTO 'Status' (statusId, status)
        VALUES(?, ?)
        ''', (row['statusId'], row['status']))

conn.commit()
cur.close()
conn.close()
