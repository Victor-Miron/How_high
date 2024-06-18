import pandas as pd
import sqlite3

def create_and_insert_table(conn, table_name, df):
    """
    Create a table and insert data from a DataFrame into the table.

    Parameters:
    conn (sqlite3.Connection): SQLite connection object.
    table_name (str): Name of the table to be created.
    df (pd.DataFrame): DataFrame containing the data to be inserted.
    """
    cur = conn.cursor()

    # Generate column definitions for the table creation SQL command
    columns = ', '.join([f"{col} TEXT" for col in df.columns])
    cur.execute(f'''
        CREATE TABLE IF NOT EXISTS {table_name} (
            {columns}
        )
    ''')

    # Insert data into the table
    for index, row in df.iterrows():
        placeholders = ', '.join(['?'] * len(row))
        cur.execute(f'''
            INSERT INTO {table_name} ({', '.join(df.columns)})
            VALUES ({placeholders})
        ''', tuple(row))

    conn.commit()
    print(f"Data inserted successfully into the {table_name} table.")

# Connect to the SQLite database or create one if it doesn't exist
conn = sqlite3.connect('Greatest.db')

# List of CSV files and corresponding table names
csv_files_and_tables = [
    ('archive/circuits.csv', 'Circuits'),
    ('archive/constructor_results.csv', 'Constructor_results'),
    ('archive/constructor_standings.csv', 'Constructor_standings'),
    ('archive/constructors.csv', 'Constructors'),
    ('archive/drivers.csv', 'Drivers')
]

# Loop through each CSV file and table name
for file_path, table_name in csv_files_and_tables:
    # Read the CSV file into a DataFrame
    try:
        df = pd.read_csv(file_path)
        # Create table and insert data
        create_and_insert_table(conn, table_name, df)
    except Exception as e:
        print(f"An error occurred while processing {file_path}: {e}")

# Close the connection
conn.close()

