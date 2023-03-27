import math

from IO_module.output_block import output_init

ans = 0


def bisection_method(func, a, b, eps):
    x0 = (a + b) / 2
    n = int(math.log2(abs(a - b) / eps)) + 1
    for i in range(n):
        if func(x0) * func(a) < 0:
            tmp = x0
            x0 = (x0 + a) / 2
            b = tmp
        else:
            tmp = x0
            x0 = (x0 + b) / 2
            a = tmp
    ans = x0
    output_init(func, a, b, ans)
