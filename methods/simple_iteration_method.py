from IO_module.output_block import output_init
from service.derivative import df_dx

ans = 0


def check_convergence_simple_iteration_method(func, a, b):
    # проверяем достаточное условие сходимости метода простой итерации
    # на интервале [a, b]
    x = (a + b) / 2  # выбираем произвольную точку на интервале
    phi_derivative = df_dx(lambda x: x - func(x), x)

    if abs(phi_derivative) >= 1:
        return False
    else:
        return True


def simple_iteration_method(func, a, b, eps, description):
    def phi(x):
        return x - func(x) / df_dx(func, x)

    x0 = (a + b) / 2
    if not check_convergence_simple_iteration_method(func, a, b):
        print("Метод расходится на данном интервале")
        return None
    # Начало итерационного процесса
    x_prev = x0
    x_curr = phi(x_prev)
    iterations = 1
    while abs(x_curr - x_prev) >= eps:
        x_prev = x_curr
        x_curr = phi(x_prev)
        iterations += 1

    print(f"Метод простой итерации для уравнения {description}:")
    print(f"Корень уравнения на отрезке [{a}, {b}]: {x_curr}")
    print(f"Количество итераций: {iterations}")
    output_init(func, a, b, x_curr, description)
