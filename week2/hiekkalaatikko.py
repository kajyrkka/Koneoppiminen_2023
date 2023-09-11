import numpy as np
import matplotlib.pyplot as plt

koe = np.zeros((2,6))


koko = koe.shape
print("koe shape = ", koko)

rivit = koko[0]
sarakkeet = koko[1]

for r in range(rivit):
    for s in range(sarakkeet):
        koe[r][s] = 100


koe[0][:] = np.arange(1,7,1)

print(koe)

#koe[0][1] = 100
#koe[1][:] = np.zeros(3)
#koe[1][0:3] = np.ones(2)
#print(koe.shape)
#print("koe =",koe)

