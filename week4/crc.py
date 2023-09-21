import numpy as np


def crc(data):
    m0 = 0
    m1 = 0
    m2 = 0
    for i in range(len(data)):
        kooderiin = np.logical_xor(data[i],m2).astype(int)
        m2 = m1
        m1 = np.logical_xor(kooderiin,m0).astype(int)
        m0 = kooderiin
        print(m0," ",m1, " ", m2)
    return m2,m1,m0
    





input = np.random.randint(0,2,10)
m2,m1,m0 = crc(input)
output = np.zeros(13)
output[0:10]= input
output[10]= m2
output[11]= m1
output[12]= m0

# tehdään virhe
output[5] = np.logical_xor(output[5],1).astype(int)

print(input)
print(output)
print("output ajettuna uudelleen crc tarkisteeseen = ", crc(output))
