import numpy as np
from numpy import sum 
import random

#Matrix dimention:
x=128

m1 = np.random.randint(0,10,(x,x))
m2 = np.random.randint(0,10,(x,x))

print (np.add(m1,m2))