import numpy as np

import matplotlib.pyplot as plt

t = np.arange(0,1,0.001)
sig = np.cos(2*np.pi*5*t)
sig2 = np.power(sig,2)
sig3 = np.power(sig,3)

fig, ax = plt.subplots(figsize=(5, 3), layout='constrained')
ax.plot(sig,'-r', label='linear')  # Plot some data on the axes.
ax.plot(sig2,'*g', label='quadratic')  # Plot more data on the axes...
ax.plot(sig3,'.b', label='cubic')  # ... and some more.
ax.set_xlabel('x label')  # Add an x-label to the axes.
ax.set_ylabel('y label')  # Add a y-label to the axes.
ax.set_title("Simple Plot")  # Add a title to the axes.
ax.legend()  # Add a legend.
plt.show()


fig, ax2 = plt.subplots(figsize=(5, 2.7), layout='constrained')
categories = ['turnips', 'rutabaga', 'cucumber', 'pumpkins']

ax2.bar(categories, np.random.rand(len(categories)))
plt.show()

