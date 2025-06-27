from matplotlib.pyplot import *
from numpy import *

x = linspace(-10, 10, 100)

y = x / 2 - 2

plot(x, y, label="f(x) = x/2 - 2")
scatter(0, -2, color='red', label="Interseção Y (0,-2)")
scatter(4, 0, color='blue', label="Interseção X (4,0)")
axhline(0, color='black', linewidth=0.5)
axvline(0, color='black', linewidth=0.5)
title("Questão 3")
grid()
legend()
show()