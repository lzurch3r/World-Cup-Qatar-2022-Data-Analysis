# -*- coding: utf-8 -*-
# import libraries
import pandas as pd
# import numpy as np

# Create variable DataFrame from Pandas library
path = r'C:\Users\Lev\Documents\Git\World-Cup-Qatar-2022-Data-Analysis\Fifa_world_cup_matches.csv'
df = pd.read_csv(path)

## Answer Question 1: How many total in-game penalty goals were scored from the start of the Quarter-finals up to and including the Final game?
# Step 1: filter out data by rows labelled "Quarter-final", "Semi-final", "Play-off for third place", "Final" from column "category"
dfPenalties = df[df["category"].isin(["Quarter-final", "Semi-final", "Play-off for third place", "Final"])]

# Step 2: grab data from columns labelled "penalties scored team1", "penalties scored team2"
sumPenalties = dfPenalties.sum()

# Step 3: sum of values from columns into variable
total = sumPenalties["penalties scored team1"] + sumPenalties["penalties scored team2"]

# Step 4: Output question and variable answer
print("Q: How many total in-game penalty goals were scored from the start of the Quarter-finals up to and including the Final game?")
print("A: " + str(total))

## Answer Question 2: What three teams incurred the most fouls across the whole World Cup 2022?
# Step 1: create dataframes grouped by teams ("team1", "team2")
sTeam1 = df.groupby("team1")["fouls against team2"].sum()
sTeam2 = df.groupby("team2")["fouls against team1"].sum()

# Add the two series together
sFouls = sTeam1 + sTeam2

# Step 2: group together the top three teams according to the sorted data
sFouls = sFouls.sort_values(ascending = False)
mostFouls = [0, 1, 2]
for i in mostFouls:
    mostFouls[i] = sFouls.index[i]

# Step 3: Display the names of the three teams
print("Q: What three teams incurred the most fouls across the whole World Cup 2022?")
print("1st Place: " + str(mostFouls[0]))
print("2nd Place: " + str(mostFouls[1]))
print("3rd Place: " + str(mostFouls[2]))

##DONE :)