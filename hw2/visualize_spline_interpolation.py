import numpy as np
from matplotlib import pyplot as plt
from scipy.interpolate import CubicSpline

# x_original = np.array([-1, -0.5, 0, 0.5, 1])
# y_original = np.abs(x_original)

step = input("введи значение шага h (0.2, 0.1, или 0.05): \n")
step = float(step)

a = -1.0 
b = 1.0

n = int((b - a) / step) + 1 # к-во узлов интерполяции

# это массив узлов интерполяции и значений функции y = |x| в них
x_original = [round(a + i * step, 5) for i in range(0, n)]
y_original = [abs(x) for x in x_original] 

# создание кубического сплайна 
cs = CubicSpline(x_original, y_original)

# сетка для построения гладкого графика
x_smooth = np.linspace(-1, 1)
y_smooth = cs(x_smooth) # значения кубического сплайна в точках сетки x_smooth

# графики
plt.plot(x_smooth, np.abs(x_smooth), 'k-', label='y = $|x|$')
plt.plot(x_smooth, y_smooth, 'r--', label='кубический сплайн')
plt.scatter(x_original, y_original, color='blue', zorder=3, label='узлы интерполяции')

# внешний вид графика
plt.xlabel('x')
plt.ylabel('y')
plt.title('Интерполяция функции $|x|$ кубическим сплайном')
plt.legend()
plt.grid(True)

# сохраняю график в файл перед отображением
plt.savefig('cubic_spline_interpolation_test.png')

plt.show()

