import pandas as pd

dfPlayers = pd.read_csv("PlayerCities.csv", sep=",", usecols=[2,9])
#dfPlayersTeam = pd.read_csv("Nationalities.csv", sep=",", usecols=[2])
#dfPlayers = dfPlayers.groupby(['Nationality']).size().reset_index(name='count')


#dfteamMap = pd.concat([dfPlayers, dfPlayersTeam], axis=1, join='inner')

dfteamMap = dfPlayers.groupby(['Team', 'Nationality' ]).size().reset_index(name='count')

dfPoints = pd.read_csv("Points.csv", nrows=50, sep=";")
dfTeams = pd.read_csv("2020-2021Team.csv", nrows=50, sep=",")