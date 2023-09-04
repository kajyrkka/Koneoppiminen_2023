import numpy as np
import matplotlib.pyplot as plt
#from sakarapulssi import sakara
import sakarapulssi as S

t,tulos = S.sakara(100,6)
plt.figure(1)
plt.plot(t,tulos)
plt.show()


