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
# Step 1: sort data from columns labelled ()