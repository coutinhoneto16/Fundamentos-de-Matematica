from matplotlib.pyplot import *
from numpy import *

x = linspace(-10, 10, 100)

y = x**2 - 4

plot(x, y, label="f(x) = x² - 4")
scatter(0, -4, color='red', label="Interseção Y (0,-4)")
scatter(-2, 0, color='blue', label="Interseção X (-2,0)")
scatter(2, 0, color='blue', label="Interseção X (2,0)")
axhline(0, color='black', linewidth=0.5)
axvline(0, color='black', linewidth=0.5)
title("Questão 4")
grid()
legend()
show()