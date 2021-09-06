import pandas as pd

dfplayercities = pd.read_csv("PlayerCities.csv", sep=",", usecols=[9])
dfplayercities = dfplayercities.groupby(['Nationality']).size().reset_index(name='count')
dfPoints = pd.read_csv("Points.csv", nrows=50, sep=";")
dfGoals = pd.read_csv("Goals.csv", nrows=50, sep=";")
dfTeams = pd.read_csv("2020-2021Team.csv", nrows=50, sep=",")