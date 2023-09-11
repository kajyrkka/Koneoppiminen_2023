import numpy as np
import matplotlib.pyplot as plt

koe = np.ones((3,4))

#print(koe)
#print(koe.reshape(2,6))

uusi = koe.reshape(2,6)
uusi[::]= np.zeros((2,6))
print(koe)
print(uusi)