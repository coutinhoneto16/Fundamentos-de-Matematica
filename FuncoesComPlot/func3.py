#- f(x) = 0,5x - 2
from matplotlib.pyplot import *
from numpy import *

x = linspace(-10, 10, 100)

y = x / 2 - 2

plot(x,y)
grid()
show()
