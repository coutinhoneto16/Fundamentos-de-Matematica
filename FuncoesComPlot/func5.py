#- f(x) = -2x² + 3x + 1
from matplotlib.pyplot import *
from numpy import *

x = linspace(-10, 10, 100)

y = (-2 * x**2) + (3 * x) + 1

plot(x,y)
grid()
show()
