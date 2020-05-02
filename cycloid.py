from numpy import sin, cos, pi, linspace
from scipy.integrate import odeint
import matplotlib.pyplot as plt
t = linspace(0, 8, 1001)

def cycloid(y, t, E, B, m, Q, omega):
     h, auxh, z, auxz = y
     dydt = [auxh, omega*auxz, auxz, omega*(E/B)-auxh]
     return dydt

E = 1
B = 1
m = 10**(-20)
Q = 1.6*10**(-19)
omega = Q*B/m
y0 = [0, 0, 0, 0]

sol = odeint(cycloid, y0, t, args=(E, B, m, Q, omega))


plt.plot(sol[:, 0], sol[:, 2], 'b', label='path of charge')
plt.legend(loc='best')
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.ylim(0, 5)
plt.xlim(0,100)
plt.show()

