import pandas as pd

dfPlayers = pd.read_csv("Players.csv", sep=",", usecols=[2,9])
dfteamMap = dfPlayers.groupby(['Team', 'Nationality' ]).size().reset_index(name='count')

dfPoints = pd.read_csv("Points.csv", nrows=50, sep=";")
dfTeams = pd.read_csv("2020-2021Team.csv", nrows=50, sep=",")