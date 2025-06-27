from matplotlib.pyplot import *
from numpy import *

x = linspace(-10, 10, 100)

y = -3 * x + 4

plot(x, y, label="f(x) = -3x + 4")
scatter(0, 4, color='red', label="Interseção Y (0,4)")
scatter(4/3, 0, color='blue', label="Interseção X (4/3,0)")
axhline(0, color='black', linewidth=0.5)
axvline(0, color='black', linewidth=0.5)
title("Questão 2")
grid()
legend()
show()