from numpy import sin, cos, pi, linspace
from scipy.integrate import odeint
import matplotlib as mpl
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

t = linspace(0, 3.8, 1001)

def symmtop(y, t, I1, I3, M, g, h):
     theta, auxtheta, phi, auxphi, psi, auxpsi = y
     dydt = [auxtheta, 1/I1*(sin(theta)*(I1*auxphi*cos(theta)-I3*auxphi**2*cos(theta)-I3*auxphi*auxpsi+0.5*I3*M*g*h)), 
             auxphi, -1/(I1*sin(theta)**2+I3*cos(theta)**2)*(2*I1*auxtheta*auxphi*sin(theta)*cos(theta)-2*I3*auxtheta*auxphi*sin(theta)*cos(theta)+I3*auxpsi*auxtheta*sin(theta)), 
             auxpsi, -auxphi*cos(theta)+auxtheta*phi*sin(theta)]
     return dydt

I1 = 2; #I1 = I2 for symmetric top
I3 = 1;
M = 1; # mass of top
g = 9.8 #acceleration due to gravity
h = 0.5 #height of center of mass
y0 = [pi/4, 100, pi/4, 1, pi/4, 1] #initial conditions

sol = odeint(symmtop, y0, t, args=(I1, I3, M, g, h))


mpl.rcParams['legend.fontsize'] = 10

fig = plt.figure()
ax = fig.gca(projection='3d')
x = sol[:, 3]*sin(sol[:, 0])*sin(sol[:, 4])+sol[:, 1]*cos(sol[:, 4])
y = sol[:, 3]*sin(sol[:, 0])*sin(sol[:, 4])-sol[:, 1]*sin(sol[:, 4])
z = sol[:, 3]*cos(sol[:, 0])+sol[:, 5]
ax.plot(x, y, z, label='angular velocity projected on Eulerian axes')
ax.legend()
plt.xlabel('x1')
plt.ylabel('x2')
plt.show()
axis('equal')


