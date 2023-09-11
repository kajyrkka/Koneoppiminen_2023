import numpy as np
import matplotlib.pyplot as plt

vastaanotettu = complex(0.5,0.5)

h = complex(0.5,0.5)

korjattu = vastaanotettu * complex(0.5,-0.5)
print("korjattu = ", korjattu)

amplitudikorjattu = korjattu / np.power(np.abs(h),2)
print("amplitudikorjattu = ", amplitudikorjattu)