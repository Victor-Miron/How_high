import sqlite3
import matplotlib.pyplot as plt

# Connect to sql database
conn = sqlite3.connect('Greatest.db')
cur = conn.cursor()

# Fetch data for the first two teams with maximum wins
cur.execute("""SELECT name, sum(wins) AS "Total wins", MIN(year) AS "Year started", 
        max(year) AS "Year ended",
        (max(year) - min(year)) AS "Total years"
        FROM "Constructor Data"
        GROUP by name
        ORDER by "Total wins" DESC
        LIMIT 2; 
""")

team_data = cur.fetchall()

# Close connection
conn.close()

# Process data into separate lines
team_names = [team[0] for team in team_data]
total_wins = [team[1] for team in team_data]
years_started = [team[2] for team in team_data]
years_ended = [team[3] for team in team_data]
total_years = [team[4] for team in team_data]

# Calculate average wins per year using dictionaries
average_wins_per_year = {team_names[i]: total_wins[i] / total_years[i] for i in range(len(team_names))}

# Display result
print("\nTeams:", team_names)
print("Total Wins:", total_wins)
print("Years Started:", years_started)
print("Years Ended:", years_ended)
print("Total Years:", total_years)
print("\nAverage Wins Per Year")
for team, avg_wins in average_wins_per_year.items():
    print(f"{team}: {avg_wins:.2f}")

# Plot total wins for each team
plt.figure(figsize=(10, 6))
plt.bar(team_names, total_wins, color=['#1f77b4', '#ff7f0e'])
plt.title("Total Wins for top 2 Teams")
plt.xlabel("Teams")
plt.ylabel("Total Wins")
plt.show()

# Plot wins over time for each team
plt.figure(figsize=(12, 6))
for i, team in enumerate(team_names):
    plt.plot([years_started[i], years_ended[i]], [0, total_wins[i]], marker='o', label=team)

plt.title("Wins Over Time for Top 2 Teams")
plt.xlabel("Year")
plt.ylabel("Wins")
plt.legend()
plt.show()
