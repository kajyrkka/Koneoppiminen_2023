import pandas as pd

column_names = ['signaali']
#df = pd.read_csv("aani.csv",names=column_names)
df = pd.read_csv("hairio.csv",names=column_names)

sig = df['signaali'].astype(float).to_numpy()

