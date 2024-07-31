import sqlite3
import pandas as pd

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
        LIMIT 2; """

max_team_points_data = pd.read_sql_query(max_team_points, conn)

# Selecting the team with maximum points hall of fame
team_hall_of_fame_points = """SELECT name, nationality, standings_points, year FROM "Constructor Data"
            WHERE standings_points = (SELECT max(standings_points) FROM "Constructor Data");"""

team_hall_of_fame_points_data = pd.read_sql_query(team_hall_of_fame_points, conn)

# finding all team nationalities during all years
nationalities = """SELECT 
    nationality, 
    GROUP_CONCAT(DISTINCT name) AS team_names, 
    COUNT(DISTINCT name) AS number_of_teams
    FROM "Constructor Data"
    GROUP BY nationality
    ORDER BY number_of_teams DESC;"""

# Drivers Data
# calculating top 3 with the most points in their career
top_three = """SELECT forename, surname, sum(points) AS "Total Points", (max(year) - min(year))  As "Duration years" 
    FROM Drivers_Data
    GROUP by forename, surname
    ORDER by "Total Points" DESC
    Limit 3;"""

# # finding top 3 drivers with points in f1 existence
# cur.execute("""SELECT forename, surname, sum(points) AS "Total Points", year FROM "Drivers Data"
# GROUP by forename, surname, year
# ORDER by "Total Points" DESC
# limit 3;
# """)

# comparing first 3 drivers how many points had in their career every year
points_comparison = """SELECT forename, surname, sum(points) AS "Total Points", year FROM Drivers_Data
    WHERE (forename = "Lewis" AND surname= "Hamilton") or (forename = "Max" AND surname = "Verstappen")
    or (forename = "Sebastian" AND surname= "Vettel")
    GROUP by forename, surname, year
    ORDER by year DESC;"""

points_comparison_data = pd.read_sql_query(points_comparison, conn)

# finding all nationalities of the drivers along the years
driver_nationalities = """SELECT Nationality, 
    COUNT(DISTINCT forename || ' ' || surname) AS number_of_drivers
    FROM Drivers_Data
    GROUP BY Nationality
    ORDER BY number_of_drivers DESC;"""

driver_nationalities_data = pd.read_sql_query(driver_nationalities, conn)

# finding the most winning drivers at every circuit
circuit_winners = """SELECT (forename || ' ' || surname) AS Name, sum(rank) AS "Total Wins" , "Circuit Name" 
    FROM Drivers_Data
    WHERE rank=1
    GROUP by Name, "Circuit Name"
    ORDER by "Total Wins" DESC;"""

circuit_winners_data = pd.read_sql_query(circuit_winners, conn)
conn.close()
