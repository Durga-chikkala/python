import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
data=pd.read_csv("/content/matches.csv")
data.head(10)
data.shape
data.columns
data.isna().any()
data.describe()
data['id'].count()
data['season'].unique()
data.tail()
data.iloc[data['win_by_runs'].idxmax()]
data.iloc[data['win_by_wickets'].idxmax()]
probability_win=data['toss_winner']==data['winner']
probability_win.groupby(probability_win).size()
data["city"].value_counts()
data['player_of_match'].value_counts()
data["toss_decision"].value_counts()
