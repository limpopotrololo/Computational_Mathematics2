def df_dx(func, x):
    delta_x = 10 ** -6
    return (func(x + delta_x) - func(x)) / delta_x


def df_dx_2(func, x):
    h = 0.001
    # print((-func(x + 2 * h) + 16 * func(x + h) - 30 * func(x) + 16 * func(x - h) - func(x - 2 * h)) / 12 * h ** 2)
    # print((func(x + h) - 2 * func(x) + func(x - h)) / h ** 2)
    # # return (func(x + h) - 2 * func(x) + func(x - h)) / h ** 2
    return (-func(x + 2 * h) + 16 * func(x + h) - 30 * func(x) + 16 * func(x - h) - func(x - 2 * h)) / 12 * h ** 2


# def max_df_dx(func,a,b):
#
#     return max(range(a,b,0.01), key=df_dx(func))
