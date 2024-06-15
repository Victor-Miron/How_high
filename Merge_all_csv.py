import pandas as pd
import glob
import os
import sqlite3

# folder containing the CSV files
folder = 'archive'

# Find all CSV files in a folder
csv_files = glob.glob(os.path.join(folder, '*.csv'))

# Read each CSV file into a Data Frame and store them in a list
dfs = [pd.read_csv(file) for file in csv_files]

# Concatenate all DataFrames into one
merged_df = pd.concat(dfs, ignore_index=True)

# Create one big CSV file
merged_df.to_csv('merged.csv', index=False)