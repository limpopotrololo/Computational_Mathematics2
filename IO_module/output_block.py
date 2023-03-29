import matplotlib.pyplot as plt
import numpy as np


def print_graph(f, a, b, ans, description):
    x = np.arange(a - 2, b + 2, 0.01)
    # Вычисляем значения функции  для каждого значения аргумента
    y = []
    for i in x:
        y.append(f(i))

    # Создаем объекты Figure и Axes для отображения графика
    fig, ax = plt.subplots(figsize=(10, 8), dpi=300)
    # Отображаем график функции
    ax.plot(x, y, label=description)
    # Устанавливаем границы отображения по осям x и y с запасом
    ax.set_xlim([a - abs(a) * 0.1, b + abs(b) * 0.1])
    ax.set_ylim([min(y) - abs(min(y)) * 0.1, max(y) + abs(max(y)) * 0.1])
    ax.axvline(a, color='blue', linewidth=1)
    ax.axvline(b, color='blue', linewidth=1)
    ax.axhline(0, color='red', linewidth=1)

    ax.minorticks_on()
    ax.grid(which='major',
            color='k')

    ax.grid(which='minor',
            color='k',
            linewidth=0.2)

    ax.legend(loc='upper right', shadow=True, fontsize='large')

    # Настраиваем параметры шрифта
    plt.rcParams.update({'font.size': 16})

    # Добавляем название графика и осей
    ax.set_title('График жирафик')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    plt.scatter([ans], [0], color="red", linewidths=0.1, zorder=10)
    plt.show()


def output_init(func, a, b, ans, descripton):
    print_graph(func, a, b, ans, descripton)
