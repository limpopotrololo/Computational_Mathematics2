from service import settings as st
from methods.bisection_method import bisection_method
from methods.secant_method import secant_method
from methods.simple_iteration_method import simple_iteration_method


def set_interval(eq):
    row_a = None
    row_b = None
    root_not_exist = True
    while root_not_exist:
        row_a = float(input("Введите левую границу интервала\n"))
        row_b = float(input("Введите правую границу интервала\n"))
        if eq(row_a) * eq(row_b) <= 0:
            print(eq(row_a) * eq(row_b))
            root_not_exist = False
        else:
            print("Некорректный интервал")
    return row_a, row_b


def set_epsilon(a, b):
    row_eps = None
    flag = True
    while flag:
        row_eps = float(input("Введите погрешность\n"))
        if b > row_eps > a:
            break
        print("Некорректная погрешность")
    return row_eps


def init():
    eq_flag = -1
    mtd_flag = -1
    print("\nВыбирите уравнение:")
    print("_________________________________________")
    print("(1) " + st.description1)
    print("(2) " + st.description2)
    print("(3) " + st.description3)
    print("(4) " + st.description4)

    print("_________________________________________\n")

    while eq_flag > 4 or eq_flag < 1 or int(eq_flag) != eq_flag:
        eq_flag = int(input("Введите номер уравнения 1-4\n"))
    # TODO: вывести названия методов в settings.py
    print("Список методов:")
    print("_________________________________________\n")
    print("(1) Метод половинного деления")
    print("(2) Метод секущих")
    print("(3) Метод простой итерации")
    print("_________________________________________\n")

    while mtd_flag > 3 or mtd_flag < 1 or int(mtd_flag) != mtd_flag:
        mtd_flag = int(input("Введите номер метода 1-3\n"))

    a, b = set_interval(st.equations[eq_flag])
    print(st.descriptions[eq_flag])
    # TODO: сделать вариантивный выбор точности (она должна зависеть от выбора метода и в приниципе ее нужно выбирать
    eps = 0.00001
    if mtd_flag == 1:
        bisection_method(st.equations[eq_flag], a, b, eps, st.descriptions[eq_flag])
    elif mtd_flag == 2:
        secant_method(st.equations[eq_flag], a, b, eps, st.descriptions[eq_flag])
    elif mtd_flag == 3:
        simple_iteration_method(st.equations[eq_flag], a, b, eps, st.descriptions[eq_flag])
