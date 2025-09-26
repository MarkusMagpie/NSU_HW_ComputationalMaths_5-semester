import math

epsilon = pow(10, -8)
right = 0
left = 1


def f(x, a, b, c):
    return x ** 3 + a * x ** 2 + b * x + c

def sign(x):
    if x < 0:
        return -1
    else:
        return 1

# дискриминант производной кубического уравнения: f'(x) = 3x^2 + 2ax + b 
# D = (2a)^2 - 4*3*b
def discriminant_derivative(a, b):
    return 4 * a ** 2 - 12 * b

# бисекция для поиска корня на отрезке [a, b]
def bisectional_root_search(a, b, c1, c2, c3):
    # разные знаки f(a) и f(b) - условие существования корня!
    if sign(f(a, c1, c2, c3)) == sign(f(b, c1, c2, c3)):
        raise Exception("a and b do not bound a root")

    m = (a + b) / 2

    if abs(f(m, c1, c2, c3)) <= epsilon:
        return m
    elif abs(a - b) < epsilon:
        return a
    # если f(m) и f(b) имеют разные знаки, то рекурсивно ищется корень на [m, b]
    elif sign(f(m, c1, c2, c3)) != sign(f(b, c1, c2, c3)):
        return bisectional_root_search(m, b, c1, c2, c3)
    elif sign(f(m, c1, c2, c3)) != sign(f(a, c1, c2, c3)):
        return bisectional_root_search(a, m, c1, c2, c3)

# поиск отрезка где функция имеет на концх разные знаки -> наличие корня
def find_interval(left_bound, right_bound, direction, a, b, c):
    if direction == right:
        step = 1
    else:
        step = -1

    while sign(f(left_bound, a, b, c)) == sign(f(right_bound, a, b, c)):
        left_bound += step
        right_bound += step
    if f(left_bound, a, b, c) == 0:
        return left_bound
    elif f(right_bound, a, b, c) == 0:
        return right_bound
    else:
        return bisectional_root_search(left_bound, right_bound, a, b, c)
    
def find_single_root(a, b, c):
    if abs(f(0, a, b, c)) <= epsilon:
        return [0]
    if f(0, a, b, c) < -epsilon:
        return [find_interval(0, 1, right, a, b, c)]
    return [find_interval(-1, 0, left, a, b, c)]

def find_multiple_roots(a, b, c):
    x_1 = (-2 * a - math.sqrt(discriminant_derivative(a, b))) / 6
    x_2 = (-2 * a + math.sqrt(discriminant_derivative(a, b))) / 6
    f_x1 = f(x_1, a, b, c)
    f_x2 = f(x_2, a, b, c)

    if abs(f_x1) <= epsilon and abs(f_x2) <= epsilon:
        return [x_1, x_2]
    if abs(f_x1) <= epsilon:
        return [x_1, find_interval(x_2, x_2 + 1, right, a, b, c)]
    if abs(f_x2) <= epsilon:
        return [x_2, find_interval(x_1 - 1, x_1, left, a, b, c)]
    if (f_x1 > epsilon and f_x2 < -epsilon):
        return [
            find_interval(x_1 - 1, x_1, left, a, b, c),
            bisectional_root_search(x_1, x_2, a, b, c),
            find_interval(x_2, x_2 + 1, right, a, b, c)
        ]
    if (f_x1 < -epsilon):
        return [find_interval(x_2, x_2 + 1, right, a, b, c)]
    return [find_interval(x_1 - 1, x_1, left, a, b, c)]

def solve_equation(a, b, c):
    roots = []
    if discriminant_derivative(a, b) <= 0:
        roots = find_single_root(a, b, c)
    else:
        roots = find_multiple_roots(a, b, c)
    
    if len(roots) == 1:
        print(f"equation has one root: x = {roots[0]}")
    elif len(roots) == 2:
        print(f"equation has two roots: x_1 = {roots[0]}, x_2 = {roots[1]}")
    else:
        print(f"equation has three roots: x_1 = {roots[0]}, x_2 = {roots[1]}, x_3 = {roots[2]}")
    exit()

# input parameters: a, b, c; where x^3 + ax^2 + bx + c = 0
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

print(f"equation: x^3 + {a}*x^2 + {b}*x + {c} = 0\n")

solve_equation(a, b, c)