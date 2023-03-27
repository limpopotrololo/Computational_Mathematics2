import math

from methods.bisection_method import bisection_method
from methods.secant_method import secant_method
from methods.simple_iteration_method import simple_iteration_method


def eq1(x):
    return math.sin(x ** 2 + math.cos(x))


def eq2(x):
    return x ** 3 + 4.81 * x ** 2 - 17.37 * x + 5.38


def eq3(x):
    return 3 * x ** 5 - 5 * x ** 4 - 3.32 * x ** 3 + x ** 2 - 7.234 * x + 1


def eq4(x):
    return math.sin(x * 4) + math.cos(x)


equations = {
    1: eq1,
    2: eq2,
    3: eq3,
    4: eq4,
}


def set_interval(eq):
    root_not_exist = True
    while root_not_exist:
        row_a = float(input("Введите левую границу интервала\n"))
        row_b = float(input("Введите правую границу интервала\n"))
        if eq(row_a) * eq(row_b) <= 0:
            print(eq(row_a) * eq(row_b))
            root_not_exist = False
        print(eq(row_a) * eq(row_b))
        print("Некорректный интервал")
    return row_a, row_b


def set_epsilon(a, b):
    flag = True
    while flag:
        row_eps = float(input("Введите погрешность\n"))
        if row_eps < b and row_eps > a:
            flag = False
            break
        print("Некорректная погрешность")
    return row_eps


def init():

    eq_flag = -1
    mtd_flag = -1
    print("\nВыбирите уравнение:")
    print("_________________________________________")
    print("(1) y = sin(x\u00B2+cosx)")
    print("(2) y = x\u00B3 +4.81x\u00B2−17.37x + 5.38")
    print("(3) y = 3x\u2075−5x\u2074−3.32x\u00B3+x\u00B2−7.234x+1")
    print("(4) y= sinx * 4 + cosx")

    print("_________________________________________\n")

    while eq_flag > 4 or eq_flag < 1 or int(eq_flag) != eq_flag:
        eq_flag = int(input("Введите номер уравнения 1-4\n"))

    print("Список методов:")
    print("_________________________________________\n")
    print("(1) Метод половинного деления")
    print("(2) Метод секущих")
    print("(3) Метод простой итерации")
    print("_________________________________________\n")

    while mtd_flag > 3 or mtd_flag < 1 or int(mtd_flag) != mtd_flag:
        mtd_flag = int(input("Введите номер метода 1-3\n"))

    a, b = set_interval(equations[eq_flag])
    eps = 0.00001
    if mtd_flag == 1:
        bisection_method(equations[eq_flag], a, b, eps)
    elif mtd_flag == 2:
        secant_method(equations[eq_flag], a, b, eps)
    elif mtd_flag == 3:
        simple_iteration_method(equations[eq_flag], a, b, eps)
