#  James Ridley CST 305
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

#  modeling after cpu utilization given by 1-p^n
# n = the number or processes running
# p = the average percentage of time spent waiting for I/O
def CPU(p, n):
   n = 10
   ddp = -n*(p**(n-1))
   return ddp

# initial conditions

p0 = 1

# timeline in seconds

t = np.linspace(0, 50)

#  solving the ODE

p = odeint(CPU,p0,t)
 #  visualization
print(t, p)
plt.plot(t,p)
plt.xlabel('time')
plt.ylabel('% of time spent waiting')
plt.show()

