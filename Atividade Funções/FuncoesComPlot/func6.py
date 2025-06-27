from matplotlib.pyplot import *
from numpy import *

x = linspace(-10, 10, 100)

y = (x**2) + (2 * x) + 1    

plot(x, y, label="f(x) = x² + 2x + 1")
scatter(0, 1, color='red', label="Interseção Y (0,1)")
scatter(-1, 0, color='blue', label="Interseção X (-1,0)")
axhline(0, color='black', linewidth=0.5)
axvline(0, color='black', linewidth=0.5)
title("Questão 6")
grid()
legend()
show()