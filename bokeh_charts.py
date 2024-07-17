import sqlite3
import pandas as pd
from bokeh.io import show, output_file
from bokeh.plotting import figure, ColumnDataSource
from bokeh.layouts import column

# Connect to the SQLite database
conn = sqlite3.connect('Greatest.db')

cur = conn.cursor()
# See how many wins first two contractor teams have in how many years

# Teams Datas

# Selecting the first 2 teams with maximum points hall of fame and in how many years
max_team_points = """SELECT name, sum(wins) AS "Total wins", MIN(year) AS "Year started", 
        max(year) AS "Year ended",
        (max(year) - min(year)) AS "Total years"
        FROM "Constructor Data"
        GROUP by name
        ORDER by "Total wins" DESC
        limit 10; """

max_team_points_data = pd.read_sql_query(max_team_points, conn)

conn.close()

# Selecting the first 2 teams with maximum points hall of fame and in how many years
source = ColumnDataSource(max_team_points_data)

p1 = figure(x_range=max_team_points_data['name'],height=250,
            title="The first 2 teams with maximum points hall of fame",
            toolbar_location=None, tools="")
p1.vbar(x='name', top='Total wins', width=0.2, source=source)

p1.xgrid.grid_line_color = None
p1.y_range.start=0

output_file('output.html')

show(p1)