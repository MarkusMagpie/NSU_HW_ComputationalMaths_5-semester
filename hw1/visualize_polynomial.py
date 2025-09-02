import numpy as np
from matplotlib import pyplot as plt

step = input("введи значение шага h (0.2, 0.1, или 0.05): \n")
step = float(step)

a = -1.0 
b = 1.0

n = int((b - a) / step) + 1 # узлы интерполяции

xvals = [round(a + i * step, 5) for i in range(0, n)]
yvals = [abs(x) for x in xvals] 

def lagrangePolynomial(x):
    result = 0

    for i in range(0, n):
        tmp = yvals[i]
        for j in range(0, n):
            if (j != i):
                tmp *= (x - xvals[j]) / (xvals[i] - xvals[j])

        result += tmp

    return result

# plt.rcParams["figure.autolayout"] = True
plotgrid = np.linspace(-1, 1, 1000)

plt.plot(plotgrid, lagrangePolynomial(plotgrid), color='blue', linewidth=3)
for i in range(0, n):
    plt.plot(xvals[i], yvals[i], 'ro')
    # print(xvals[i], yvals[i])
    # printf("L_%d(x = %.1f) = %.6f\n", n, xvals[i], yvals[i])
    print(f"L_{n}(x = {xvals[i]:.1f}) = {yvals[i]:.6f}")

# сохраняю график в файл перед отображением
plt.savefig('lagrange_interpolation.png')

plt.show()
