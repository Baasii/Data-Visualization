import pandas as pd


dfPlayers = pd.read_csv("Players.csv", sep=",", usecols=[2,9])
dfteamMap = dfPlayers.groupby(['Team', 'Nationality' ]).size().reset_index(name='count')

dfPoints = pd.read_csv("Points.csv", nrows=50, sep=";")

dfTeams16_17 = pd.read_csv("2016-2017Team.csv", sep=",")
dfTeams17_18 = pd.read_csv("2017-2018Team.csv", sep=",")
dfTeams18_19 = pd.read_csv("2018-2019Team.csv", sep=",")
dfTeams19_20 = pd.read_csv("2019-2020Team.csv", sep=",")
dfTeams20_21 = pd.read_csv("2020-2021Team.csv", sep=",")