from numpy import sin, cos, pi, linspace
from scipy.integrate import odeint
import matplotlib.pyplot as plt
t = linspace(0, 100, 1001)

def emma(y, t, a):
     r, auxr, theta, auxtheta = y
     dydt = [auxr, r*auxr*(sin(a))**2.0-9.8*cos(a)*sin(a), auxtheta, 0]
     return dydt

a = (pi/3.0,);
y0 = [2.0, 1, 0.0, 1]

sol = odeint(emma, y0, t, args=(a))


plt.plot(sol[:, 0]*cos(sol[:, 2]), sol[:, 0]*sin(sol[:, 2]), 'b', label='path of mass')
plt.legend(loc='best')
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.axis('equal')
plt.show()


