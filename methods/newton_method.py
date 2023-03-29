from service.derivative import df_dx
from IO_module.output_block import output_init

ans = 0


def newton_method(func, a, b, eps, description):
    next_x = None
    if func(b) > 0:
        x = b
    else:
        x = a
    while abs(func(x)) > eps:
        buf = next_x
        next_x = x - func(x) / df_dx(x)
        x = buf

    output_init(func, a, b, ans, description)
