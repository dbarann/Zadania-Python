import numpy as np
from numpy import matmul 
import random

#Matrix dimention:
x=8

m1 = np.random.randint(0,10,(x,x))
m2 = np.random.randint(0,10,(x,x))

print (np.matmul(m1,m2))