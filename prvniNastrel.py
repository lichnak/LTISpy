import numpy as np
from sympy import *
from mpmath import polyroots

# state space
A = Matrix([[0, 1, 0], [0, 0, 1], [-3, -4, -2]])
B = Matrix([[0], [0], [1]])
C = Matrix([[5, 1, 0]])
D = Matrix([[0]])
s = Symbol("s")
# ss2tf
# checknout rozmery matic, invertibilitu..
dimensionA = A.shape
pomoc = s*eye(dimensionA[1]) - A
H = simplify(C * pomoc.inv()*B+D)
H_pol = Poly(H[0])
print(H)


# nuly, poly
numKoeficienty = H_pol.coeffs()
print(numKoeficienty)
print("Nuly: ")
print(polyroots(numKoeficienty))

denum = Poly(H[0] ** -1)
denKoeficienty = denum.coeffs()
print(denKoeficienty)
print("Poly: ")
print(polyroots(denKoeficienty))
#

# impulsni charakteristika


def ss2tf(params):
    "docstring"

