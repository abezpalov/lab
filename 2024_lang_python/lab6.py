"""
Лабораторная работа 6

Matplotlib
"""

import math
import tkinter

import numpy as np
import matplotlib.pyplot as plt


def draw_arch(event):

    fi = np.arange(0, np.pi * 2 * float(ent_count.get()), 0.01)
    r = float(ent_step.get()) * fi

    x = r * np.cos(fi)
    y = r * np.sin(fi)

    fig, ax = plt.subplots(figsize=(10, 10), layout='constrained')
    ax.plot(x, y, label=r'Спираль Архимеда', linestyle='-')

    ax.spines[['top', 'right']].set_visible(False)
    ax.spines[['top', 'right']].set_visible(False)
    ax.spines['bottom'].set_position('zero')
    ax.spines['left'].set_position('zero')

    arrow_fmt = dict(markersize=4, color='black', clip_on=False)
    ax.plot((1), (0), marker='>', transform=ax.get_yaxis_transform(), **arrow_fmt)
    ax.plot((0), (1), marker='^', transform=ax.get_xaxis_transform(), **arrow_fmt)

    ax.set_xlabel('x', size=14, labelpad=0, x=0.98)
    ax.set_ylabel('y', size=14, labelpad=0, y=0.98, rotation=0)

    ax.set_title('Заголовки никто не читает')
    ax.legend()

    plt.show()


def draw_func(event):
    x0 = float(ent_x0.get())
    x1 = float(ent_x1.get())

    x = np.arange(x0, x1, (x1 - x0) / 10000)
    a = float(ent_a.get())
    b = float(ent_b.get())
    c = float(ent_c.get())
    y = a - b / x - c / x ** 3

    y = np.array(y)

    fig, ax = plt.subplots(figsize=(10, 10), layout='constrained')
    ax.plot(x, y, label=r'Странная функция', linestyle='-')

    ax.spines[['top', 'right']].set_visible(False)
    ax.spines[['top', 'right']].set_visible(False)
    ax.spines['bottom'].set_position('zero')
    ax.spines['left'].set_position('zero')

    arrow_fmt = dict(markersize=4, color='black', clip_on=False)
    ax.plot((1), (0), marker='>', transform=ax.get_yaxis_transform(), **arrow_fmt)
    ax.plot((0), (1), marker='^', transform=ax.get_xaxis_transform(), **arrow_fmt)

    ax.set_xlabel('x', size=14, labelpad=0, x=0.98)
    ax.set_ylabel('y', size=14, labelpad=0, y=0.98, rotation=0)

    ax.set_title('Или читает?')
    ax.legend()

    plt.show()


if __name__ == "__main__":

    root = tkinter.Tk()
    root.title("Лабораторная 6")

    # Области
    manage_arch = tkinter.Frame(root)
    manage_arch.pack(side=tkinter.RIGHT)

    manage_func = tkinter.Frame(root)
    manage_func.pack(side=tkinter.LEFT)

    # Управление спиралью паскаля
    lb_arch = tkinter.Label(manage_arch, text='Спираль Паскаля')
    lb_arch.pack(side=tkinter.TOP)

    manage_step = tkinter.Frame(manage_arch)
    manage_step.pack(side=tkinter.TOP)
    lb_step = tkinter.Label(manage_step, text='Шаг спирали: ')
    ent_step = tkinter.Entry(manage_step)
    lb_step.pack(side=tkinter.LEFT, anchor=tkinter.W)
    ent_step.pack(side=tkinter.RIGHT, anchor=tkinter.E)

    manage_count = tkinter.Frame(manage_arch)
    manage_count.pack(side=tkinter.TOP)
    lb_count = tkinter.Label(manage_count, text='Количество витков: ')
    ent_count = tkinter.Entry(manage_count)
    lb_count.pack(side=tkinter.LEFT, anchor=tkinter.W)
    ent_count.pack(side=tkinter.RIGHT, anchor=tkinter.E)

    # Кнопка рисования
    draw_arch_button = tkinter.Button(manage_arch, text="Рисовать", width=12)
    draw_arch_button.bind("<Button-1>", draw_arch)
    draw_arch_button.pack()

    # Управление странной функцией
    lb_func = tkinter.Label(manage_func, text='Странная функция')
    lb_func.pack(side=tkinter.TOP)

    manage_a = tkinter.Frame(manage_func)
    manage_a.pack(side=tkinter.TOP)
    lb_a = tkinter.Label(manage_a, text='a: ')
    ent_a = tkinter.Entry(manage_a)
    lb_a.pack(side=tkinter.LEFT, anchor=tkinter.W)
    ent_a.pack(side=tkinter.RIGHT, anchor=tkinter.E)

    manage_b = tkinter.Frame(manage_func)
    manage_b.pack(side=tkinter.TOP)
    lb_b = tkinter.Label(manage_b, text='b: ')
    ent_b = tkinter.Entry(manage_b)
    lb_b.pack(side=tkinter.LEFT, anchor=tkinter.W)
    ent_b.pack(side=tkinter.RIGHT, anchor=tkinter.E)

    manage_c = tkinter.Frame(manage_func)
    manage_c.pack(side=tkinter.TOP)
    lb_c = tkinter.Label(manage_c, text='c: ')
    ent_c = tkinter.Entry(manage_c)
    lb_c.pack(side=tkinter.LEFT, anchor=tkinter.W)
    ent_c.pack(side=tkinter.RIGHT, anchor=tkinter.E)

    manage_x0 = tkinter.Frame(manage_func)
    manage_x0.pack(side=tkinter.TOP)
    lb_x0 = tkinter.Label(manage_x0, text='x0: ')
    ent_x0 = tkinter.Entry(manage_x0)
    lb_x0.pack(side=tkinter.LEFT, anchor=tkinter.W)
    ent_x0.pack(side=tkinter.RIGHT, anchor=tkinter.E)

    manage_x1 = tkinter.Frame(manage_func)
    manage_x1.pack(side=tkinter.TOP)
    lb_x1 = tkinter.Label(manage_x1, text='x1: ')
    ent_x1 = tkinter.Entry(manage_x1)
    lb_x1.pack(side=tkinter.LEFT, anchor=tkinter.W)
    ent_x1.pack(side=tkinter.RIGHT, anchor=tkinter.E)

    # Кнопка рисования
    draw_func_button = tkinter.Button(manage_func, text="Рисовать", width=12)
    draw_func_button.bind("<Button-1>", draw_func)
    draw_func_button.pack()

    root.mainloop()
