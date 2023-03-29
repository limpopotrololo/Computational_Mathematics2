from IO_module.output_block import output_init

ans = 0


def secant_method(func, a, b, eps, description):
    x0 = a
    x1 = b
    while abs(x1 - x0) > eps:
        tmp = x1
        x1 = x1 - (x1 - x0) * func(x1) / (func(x1) - func(x0))
        x0 = tmp
    output_init(func, a, b, x1, description)
