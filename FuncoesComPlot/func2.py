#- f(x) = -3x + 4
from matplotlib.pyplot import *
from numpy import *

x = linspace(-10, 10, 100)

y = -3 * x + 4

plot(x,y)
grid()
show()
