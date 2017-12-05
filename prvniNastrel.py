import numpy as np
from sympy import *

# state space
A = np.matrix('-1 1; 0 1')
B = np.matrix('1; 1')
C = np.matrix('1 1')
D = np.matrix('0')

