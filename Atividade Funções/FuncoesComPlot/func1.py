from matplotlib.pyplot import *
from numpy import *

x = linspace(-10, 10, 100)
y = 2 * x + 1

plot(x, y, label="f(x) = 2x + 1")
scatter(0, 1, color='red', label="Interseção Y (0,1)")
scatter(-0.5, 0, color='blue', label="Interseção X (-0.5,0)")
axhline(0, color='black', linewidth=0.5)
axvline(0, color='black', linewidth=0.5)
title("Questão 1")
grid()
legend()
show()