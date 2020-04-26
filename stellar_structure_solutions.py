#Let's code solves four coupled, first-order differential equations that model
#the properties of a star.

from numpy import linspace, pi
from scipy.integrate import odeint
import matplotlib.pyplot as plt


def system(y, r, rho, epsilon, kappa, sigma):
        #y is an array. We will numerically integrates the elements of y.
        #rho is the density of the star
        #epsilon is the energy release per unit mass per unit time
        #sigma (what is this parameter?)

            
    
    P, M, L, T = y
        #P(r) is pressure
        #M(r) is mass
        #L(r) is luminosity
        #T(r) is temperature
        
    #To simplify the ODEs, we will use the following substitutions:
    
    
    #Below are the four coupled, first-order differential equations
    dydr = [#dP/dr
            -G*M*rho/r**2,
            
            #dM/dr
            4*pi*r**2*rho,
              
            #dL/dr
            4*pi*r**2*rho*epsilon,

            #dT/dr
            -3*rho*kappa*L/(64*pi*r**2*sigma*T**3)]
            
    return dydr

#Parameters and constants are
G = 6.67*10**-11
rho = 1414 #average density of sun (mass/volume)
epsilon = 1.91*10**-4
kappa = 10**-4
sigma = 1
#initial values:
y0 = [0, 0, 0, 10000]
#  = [P, M, L, T] 

#radius over which to integrate
r = linspace(1, 6.95**8, 100)

sol = odeint(system, y0, r, args=(rho, epsilon, kappa, sigma))

#Graph of  incliniation of inner binary vs. time:
    
plt.plot(r, sol[:, 0])
#plt.yscale('log')
#plt.xscale('log')
plt.xlabel('radius (m)')
plt.ylabel('pressure (kg/m^3)')
plt.grid()
plt.show()    

plt.plot(r, sol[:, 1])
#plt.yscale('log')
#plt.xscale('log')
plt.xlabel('radius (m)')
plt.ylabel('mass (kg)')
plt.grid()
plt.show()

plt.plot(r, sol[:, 2])
#plt.yscale('log')
#plt.xscale('log')
plt.xlabel('radius (m)')
plt.ylabel('luminosity (W)')
plt.grid()
plt.show()

plt.plot(r, sol[:, 3])
#plt.yscale('log')
#plt.xscale('log')
plt.xlabel('radius (m)')
plt.ylabel('temperature (K)')
plt.grid()
plt.show()
