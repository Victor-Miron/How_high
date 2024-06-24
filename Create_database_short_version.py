import pandas as pd
import sqlite3

# Connect to the SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('Greatest.db')

# Create a cursor object to execute SQL commands
cur = conn.cursor()

# Function to create tables and insert data from DataFrames
def create_table_from_df(df, table_name, schema):
    cur.execute(f'''
        CREATE TABLE IF NOT EXISTS "{table_name}" ({schema})
    ''')
    df.to_sql(table_name, conn, if_exists='replace', index=False)

# Read CSV files into DataFrames
circuits_df = pd.read_csv('archive/circuits.csv')
constructor_results_df = pd.read_csv('archive/constructor_results.csv')
constructor_standings_df = pd.read_csv('archive/constructor_standings.csv')
constructors_df = pd.read_csv('archive/constructors.csv')
drivers_df = pd.read_csv('archive/drivers.csv')
lap_times_df = pd.read_csv('archive/lap_times.csv')
pit_stops_df = pd.read_csv('archive/pit_stops.csv')
qualifying_df = pd.read_csv('archive/qualifying.csv')
races_df = pd.read_csv('archive/races.csv')
results_df = pd.read_csv('archive/results.csv')
seasons_df = pd.read_csv('archive/seasons.csv')
status_df = pd.read_csv('archive/status.csv')

# Table schemas
schemas = {
    'Circuits': '''
        circuitId INTEGER PRIMARY KEY,
        circuitRef TEXT,
        name TEXT,
        location TEXT,
        country TEXT,
        lat REAL,
        lng REAL,
        alt REAL,
        url TEXT
    ''',
    'Constructor results': '''
        constructorResultsId INTEGER PRIMARY KEY,
        raceId INTEGER,
        constructorId INTEGER,
        points INTEGER,
        status TEXT
    ''',
    'Constructor standings': '''
        constructorStandingsId INTEGER PRIMARY KEY,
        raceId INTEGER,
        constructorId INTEGER,
        points INTEGER,
        position INTEGER,
        positionText TEXT,
        wins INTEGER
    ''',
    'Constructors': '''
        constructorId INTEGER PRIMARY KEY,
        constructorRef TEXT,
        name TEXT,
        nationality TEXT,
        url TEXT
    ''',
    'Drivers': '''
        driverId INTEGER PRIMARY KEY,
        driverRef TEXT,
        number INTEGER,
        code TEXT,
        forename TEXT,
        surname TEXT,
        dob TEXT,
        nationality TEXT,
        url TEXT
    ''',
    'Lap Times': '''
        raceId INTEGER,
        driverId INTEGER,
        lap INTEGER,
        position INTEGER,
        time TEXT,
        milliseconds INTEGER
    ''',
    'Pit Stops': '''
        raceId INTEGER,
        driverId INTEGER,
        stop INTEGER,
        lap INTEGER,
        time TEXT,
        duration TEXT,
        milliseconds INTEGER
    ''',
    'Qualifying': '''
        qualifyId INTEGER PRIMARY KEY,
        raceId INTEGER,
        driverId INTEGER,
        constructorId INTEGER,
        number INTEGER,
        position INTEGER,
        q1 TEXT,
        q2 TEXT,
        q3 TEXT
    ''',
    'Races': '''
        raceId INTEGER PRIMARY KEY,
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
    ''',
    'Results': '''
        resultId INTEGER PRIMARY KEY,
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
    ''',
    'Seasons': '''
        year INTEGER PRIMARY KEY,
        url TEXT
    ''',
    'Status': '''
        statusId INTEGER PRIMARY KEY,
        status TEXT
    '''
}

# Create tables and insert data
dfs = [circuits_df, constructor_results_df, constructor_standings_df, constructors_df, drivers_df,
       lap_times_df, pit_stops_df, qualifying_df, races_df, results_df, seasons_df, status_df]

for df, (table_name, schema) in zip(dfs, schemas.items()):
    create_table_from_df(df, table_name, schema)

# Select columns from different tables and create the table Constructor Data
cur.execute(''' 
    CREATE TABLE IF NOT EXISTS "Constructor Data" AS
        SELECT Constructors.name, Constructors.nationality, 
               "Constructor standings".points, "Constructor standings".position, 
               "Constructor standings".wins, "Constructor results".points,
               Results.number, Results.grid, Results.position,
               Circuits.name AS circuit_name, Circuits.location, Circuits.country,
               Races.name AS race_name, Races.date, Seasons.year
        FROM Constructors
        INNER JOIN "Constructor standings" ON "Constructor standings".constructorId = Constructors.constructorId
        INNER JOIN "Constructor results" ON "Constructor results".constructorId = Constructors.constructorId
        INNER JOIN Results ON Results.constructorId = Constructors.constructorId
        INNER JOIN Races ON Races.raceId = Results.raceId
        INNER JOIN Circuits ON Circuits.circuitId = Races.circuitId
        INNER JOIN Seasons ON Seasons.year = Races.year;
''')

# Commit the transaction
conn.commit()

# Close the cursor and connection
cur.close()
conn.close()
