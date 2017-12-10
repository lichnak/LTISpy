import matplotlib.pyplot as plt
import sympy as sp
import numpy as np

import control_toolbox as ct

## transfer function

tf1 = ct.tf([1], [1, 3, -4])

char_poly = tf1.d_poly

print(char_poly)

print(sp.solve(char_poly))



## pendulum example with ODE
# def pend(t, y, b, c):
#     theta, omega = y
#     dydt = [omega, -b*omega - c*np.sin(theta)]
#     return dydt
#
# b = 0.25
# c = 5.0
#
# y0 = [np.pi - 0.1, 0.0]
#
# t = np.linspace(0, 20, 201)
#
#
# sol = ct.ode45(pend, t, y0, args=(b, c))
#
# plt.plot(t, sol[:, 0], 'b', label='theta(t)')
# plt.plot(t, sol[:, 1], 'g', label='omega(t)')
# plt.legend(loc='best')
# plt.xlabel('t')
# plt.grid()
# plt.show()


## characteristic polynomial from state space

# mj, mb, l, g, ti = sp.symbols('m_j, m_b, L, g, t_i')
#
# A = sp.Matrix([
#     [0, 1, 0, 0, 0],
#     [0, 0, g * mb / mj, 0, 0],
#     [0, 0, 0, 1, 0],
#     [0, 0, g * (mb - mj) / (mj * l), 0, 0],
#     [-1 / ti, 0, 0, 0, 0],
# ])
#
# B = sp.Matrix([
#     0, 1 / mj, 0, -1 / (mj * l), 0
# ])
#
# C = sp.Matrix([
#     1, 0, 0, 0, 0
# ])
#
# D = sp.Matrix([
#     0,
# ])
#
# s1 = ct.ss(A, B, C, D)
#
# print(s1.char_poly())
#
# print(s1.char_poly_coeffs())
#
# print(s1.poles())
