from numpy import linspace
from scipy.integrate import odeint
import matplotlib.pyplot as plt
t = linspace(0, 5, 1001)

def fictitious(y, t, omega):
     rx, vx, ry, vy = y
     dydt = [vx, omega**2*rx+2*omega*vy, vy, -omega**2*ry-2*omega*vx]
     return dydt

omega = 1

y0 = [-1, .2, 0, 0]

sol = odeint(fictitious, y0, t, args=(omega,))

plt.plot(sol[:, 0], sol[:, 2], 'b', label='path of mass, v0x = 0.2')
plt.legend(loc='best')
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.axis('equal')
plt.show()


