import sqlite3
# Connect to the SQLite database
conn = sqlite3.connect('Greatest.db')

cur = conn.cursor()
# See how many wins first two contractor teams have in how many years

# Teams Datas

# Selecting the first 2 teams with maximum points hall of fame and in how many years
cur.execute("""SELECT name, sum(wins) AS "Total wins", MIN(year) AS "Year started", 
        max(year) AS "Year ended",
        (max(year) - min(year)) AS "Total years"
        FROM "Constructor Data"
        GROUP by name
        ORDER by "Total wins" DESC
        LIMIT 2;
""")
# Selecting the team with maximum points hall of fame
cur.execute("""SELECT name, nationality, standings_points, year FROM "Constructor Data"
            WHERE standings_points = (SELECT max(standings_points) FROM "Constructor Data");
""")
# finding all team nationalities during all years
cur.execute("""SELECT 
    nationality, 
    GROUP_CONCAT(DISTINCT name) AS team_names, 
    COUNT(DISTINCT name) AS number_of_teams
FROM 
    "Constructor Data"
GROUP BY 
    nationality
ORDER BY 
    number_of_teams DESC;
""")

# Drivers Data
# calculating top 3 with the most points in their career
cur.execute("""SELECT forename, surname, sum(points) AS "Total Points", (max(year) - min(year))  As "Duration years" FROM "Drivers Data"
GROUP by forename, surname
ORDER by "Total Points" DESC
Limit 3;
""")

# finding top 3 drivers with points in f1 existence
cur.execute("""SELECT forename, surname, sum(points) AS "Total Points", year FROM "Drivers Data"
GROUP by forename, surname, year
ORDER by "Total Points" DESC
limit 3;
""")
# comparing first 3 drivers how many points had in their career every year
cur.execute("""SELECT forename, surname, sum(points) AS "Total Points", year FROM "Drivers Data"
WHERE (forename = "Lewis" AND surname= "Hamilton") or (forename = "Max" AND surname = "Verstappen")
or (forename = "Sebastian" AND surname= "Vettel")
GROUP by forename, surname, year
ORDER by year DESC;
""")

# finding all nationalities of the drivers along the years

cur.execute("""SELECT 
    Nationality, 
    COUNT(DISTINCT forename || ' ' || surname) AS number_of_drivers
FROM 
    "Drivers Data"
GROUP BY 
    Nationality
ORDER BY 
    number_of_drivers DESC;
""")
# finding the most winning drivers at every circuit
cur.execute("""SELECT (forename || ' ' || surname) AS Name, sum(rank) AS "Total Wins" , "Circuit Name" FROM "Drivers Data"
WHERE rank=1
GROUP by Name, "Circuit Name"
ORDER by "Total Wins" DESC;
""")
results = cur.fetchall()

for row in results:
    print(row)
conn.commit()
cur.close()
conn.close()