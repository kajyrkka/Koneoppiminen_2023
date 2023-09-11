import numpy as np
import matplotlib.pyplot as plt
from sakarapulssi import sakara as SAK
#import sakarapulssi as S
#import sakarapulssi

#t,tulos = S.sakara(100,10)
t,tulos = SAK(100,4)
#t,tulos = sakarapulssi.sakara(100,5) 
plt.figure(1)
plt.plot(t,tulos)
plt.show()


