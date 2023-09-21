import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



#df = pd.read_csv('dataoutVainOikeat.csv',usecols=['x','y','z'])
df = pd.read_csv('dataoutVainOikeat.csv',
                 delimiter='\\t',
                 header=0,
                 usecols=[1,2,3])
print(df)

colors=['red','green','blue']
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.scatter(df['x'].iloc[1:10], df['y'].iloc[1:10], df['z'].iloc[1:10],c='red')
ax.scatter(df['x'].iloc[10:20], df['y'].iloc[10:20], df['z'].iloc[10:20],c='green')
ax.scatter(df['x'].iloc[20:30], df['y'].iloc[20:30], df['z'].iloc[20:30],c='blue')
ax.scatter(df['x'].iloc[10:20], df['y'].iloc[10:20], df['z'].iloc[10:20],c='green')
ax.scatter(df['x'].iloc[30:40], df['y'].iloc[30:40], df['z'].iloc[30:40],c='black')
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

plt.show()