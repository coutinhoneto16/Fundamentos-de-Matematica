from matplotlib.pyplot import *
from numpy import *

x = linspace(-10, 10, 100)

y = (x**2) + (2 * x) + 1

plot(x,y)
grid()
show()