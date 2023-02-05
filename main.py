# -*- coding: utf-8 -*-
# import Pandas library
import pandas as pd

# Create variable DataFrame from Pandas library
filename = 'Fifa_world_cup_matches.csv' # Ensure the corresponding csv is located in the same folder as main.py
df = pd.read_csv(filename) # Reads from the csv file and stores data into a Pandas DataFrame

## Answer Question 1: How many total in-game penalty goals were scored from the start of the Quarter-finals up to and including the Final game?
# Step 1: filter out data by rows labelled "Quarter-final", "Semi-final", "Play-off for third place", "Final" from column "category"
dfPenalties = df[df["category"].isin(["Quarter-final", "Semi-final", "Play-off for third place", "Final"])]

# Step 2: grab data from columns labelled "penalties scored team1", "penalties scored team2"
sumPenalties = dfPenalties.sum() # Sums all of the values in each column

# Step 3: sum of values from columns into variable
total = sumPenalties["penalties scored team1"] + sumPenalties["penalties scored team2"]

# Step 4: Output question and variable answer
print("\nQuestion 1: How many total in-game penalty goals were scored from the start of the Quarter-finals up to and including the Final game?\n")
print("Answer: " + str(total))

## Answer Question 2: What three teams incurred the most fouls across the whole World Cup 2022?
# Step 1: Create Series grouped by teams ("team1", "team2")
sTeam1 = df.groupby("team1")["fouls against team2"].sum() # It is assumed that team1 incurred fouls against team2
sTeam2 = df.groupby("team2")["fouls against team1"].sum() # It is asusmed that team2 incurred fouls against team1

# Add the values from both series together
sFouls = sTeam1 + sTeam2 # Creates a Series in which the first column contains team names and the second column 
                         #     contains the total fouls incurred by that team

# Step 2: group together the top three teams according to the sorted data
sFouls = sFouls.sort_values(ascending = False) # Highest values appear at the top
# Use a for loop to add the three teams into an array
mostFouls = [0, 1, 2]
for i in mostFouls:
    mostFouls[i] = sFouls.index[i]

# Step 3: Display the names of the three teams
print("\nQuestion 2: What three teams incurred the most fouls across the whole World Cup 2022?\n")
print("1st Place: " + str(mostFouls[0]))
print("2nd Place: " + str(mostFouls[1]))
print("3rd Place: " + str(mostFouls[2]))

print("\nProgram finished")