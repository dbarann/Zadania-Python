import numpy as np
from numpy import linalg 
import random

#Matrix dimention:
x=5

m = np.random.randint(0,10,(x,x))

print (np.linalg.det(m))