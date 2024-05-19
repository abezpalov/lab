"""
Лабораторная работа 5. Часть 2.

Фракталы.
"""

import math
import tkinter
import tkinter.colorchooser


def set_color(event):
    global color
    _, color = tkinter.colorchooser.askcolor()


def draw(event):
    global fractal_type, color, pen_width

    def koch(order, x1, y1, x2, y2):

        global color, pen_width

        if order == 0:
            canvas.create_line(x1, y1, x2, y2, fill=color, width=pen_width.get())
        else:
            alpha = math.atan2(y2 - y1, x2 - x1)
            r = math.sqrt((x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1))

            x_a = x1 + (r / 3) * math.cos(alpha)
            y_a = y1 + (r / 3) * math.sin(alpha)
            x_c = x_a + r * math.cos(alpha - math.pi / 3) / 3
            y_c = y_a + r * math.sin(alpha - math.pi / 3) / 3
            x_b = x1 + 2 * r * math.cos(alpha) / 3
            y_b = y1 + 2 * r * math.sin(alpha) / 3

            koch(order - 1, x1, y1, x_a, y_a)
            koch(order - 1, x_a, y_a, x_c, y_c)
            koch(order - 1, x_c, y_c, x_b, y_b)
            koch(order - 1, x_b, y_b, x2, y2)

    def quadro_koch(order, x1, y1, x2, y2):

        global color, pen_width

        if order == 0:
            canvas.create_line(x1, y1, x2, y2, fill=color, width=pen_width.get())
        else:

            d_x = (x2 - x1) / 3
            d_y = (y2 - y1) / 3





            x_a = x1 + (r / 3) * math.cos(alpha)
            y_a = y1 + (r / 3) * math.sin(alpha)
            x_c = x_a + r * math.cos(alpha - math.pi / 3) / 3
            y_c = y_a + r * math.sin(alpha - math.pi / 3) / 3
            x_b = x1 + 2 * r * math.cos(alpha) / 3
            y_b = y1 + 2 * r * math.sin(alpha) / 3

            koch(order - 1, x1, y1, x_a, y_a)
            koch(order - 1, x_a, y_a, x_c, y_c)
            koch(order - 1, x_c, y_c, x_b, y_b)
            koch(order - 1, x_b, y_b, x2, y2)

    def sierpinski(order, x, y, length):

        global color

        s3d2 = math.sqrt(3) / 2

        points = [x, y, x + length / 2, y - length * s3d2, x + length, y]
        canvas.create_polygon(points, outline=color, fill=color, width=pen_width.get())

        if order > 0:
            points = [x + length / 4, y - length * s3d2 / 2, x + 3 * length / 4, y - length * s3d2 / 2,
                      x + length / 2, y]
            canvas.create_polygon(points, outline='#ffffff', fill='#ffffff', width=pen_width.get())

            sierpinski(order - 1, x, y, length / 2)
            sierpinski(order - 1, x + length / 2, y, length / 2)
            sierpinski(order - 1, x + length / 4, y - length * s3d2 / 2, length / 2)

    def get_dragon_points(order):
        x = canvas.winfo_width() / 5

        y = canvas.winfo_height() / 2
        if order == 0:
            res = list()
            res.append(x)
            res.append(y + x / 2)
            res.append(canvas.winfo_width() - x)
            res.append(y + x / 2)
            return res

        prev_res = get_dragon_points(order - 1)
        res = list()

        dir_sign = 1

        res.append(prev_res[0])
        res.append(prev_res[1])

        for i in range(0, len(prev_res) - 3, 2):
            p1x = prev_res[i]
            p1y = prev_res[i + 1]
            p2x = prev_res[i + 2]
            p2y = prev_res[i + 3]
            alpha = math.atan2(p2y - p1y, p2x - p1x) - dir_sign * math.pi / 4
            r = math.sqrt(((p1x - p2x) * (p1x - p2x) + (p1y - p2y) * (p1y - p2y)) / 2)

            pcx = p1x + r * math.cos(alpha)
            pcy = p1y + r * math.sin(alpha)

            res.append(pcx)
            res.append(pcy)
            res.append(p2x)
            res.append(p2y)

            dir_sign *= -1

        return res

    # кривая Коха
    if fractal_type.get() == 0:
        x1, y1 = 0, canvas.winfo_height()
        x2, y2 = canvas.winfo_width(), 0
        koch(fractal_power.get(), x1, y1, x2, y2)

    # Серпинский
    elif fractal_type.get() == 1:
        sierpinski(fractal_power.get(), 0, canvas.winfo_height() - 20, canvas.winfo_width() - 10)

    # Драконовая ломанная
    elif fractal_type.get() == 2:
        points = get_dragon_points(fractal_power.get())
        canvas.create_line(points, fill=color, width=pen_width.get())

    # Снежинка Коха
    elif fractal_type.get() == 3:
        padding = 100
        x1, y1 = padding, canvas.winfo_height() - padding*2.6
        x2, y2 = (canvas.winfo_width() / 2,
                  canvas.winfo_height() - padding*2.6 - canvas.winfo_width() * math.sin(math.pi / 6))
        x3, y3 = canvas.winfo_width() - padding, canvas.winfo_height() - padding*2.6
        koch(fractal_power.get(), x1, y1, x2, y2)
        koch(fractal_power.get(), x2, y2, x3, y3)
        koch(fractal_power.get(), x3, y3, x1, y1)

    # квадратная кривая Коха
    elif fractal_type.get() == 4:
        x1, y1 = 0, canvas.winfo_height()
        x2, y2 = canvas.winfo_width(), 0
        quadro_koch(fractal_power.get(), x1, y1, x2, y2)


def clear(event):
    canvas.create_rectangle(0, 0, canvas.winfo_width(), canvas.winfo_height(), outline='#ffffff', fill='#ffffff')


if __name__ == "__main__":

    root = tkinter.Tk()
    root.title("Лабораторная 5b")

    # Области
    pict = tkinter.Frame(root)
    manage = tkinter.Frame(root)
    pict.pack(side=tkinter.LEFT)
    manage.pack(side=tkinter.RIGHT)

    # Область рисования
    canvas = tkinter.Canvas(pict, width=800, height=800)
    canvas.create_rectangle(0, 0, 800, 800, outline='#ffffff', fill='#ffffff')
    canvas.pack(fill=tkinter.BOTH, expand=1)

    # Выбор фрактала
    fractal_type = tkinter.IntVar()
    fractal_type.set(0)
    fractal_type_rad0 = tkinter.Radiobutton(manage, text="Кривая Коха", variable=fractal_type, value=0)
    fractal_type_rad1 = tkinter.Radiobutton(manage, text="Салфетка Серпинского", variable=fractal_type, value=1)
    fractal_type_rad2 = tkinter.Radiobutton(manage, text="Драконова ломаная", variable=fractal_type, value=2)
    fractal_type_rad3 = tkinter.Radiobutton(manage, text="Снежинка Коха", variable=fractal_type, value=3)
    fractal_type_rad4 = tkinter.Radiobutton(manage, text="Квадрокривая Коха", variable=fractal_type, value=4)
    fractal_type_rad0.pack(side=tkinter.TOP, anchor=tkinter.W)
    fractal_type_rad1.pack(side=tkinter.TOP, anchor=tkinter.W)
    fractal_type_rad2.pack(side=tkinter.TOP, anchor=tkinter.W)
    fractal_type_rad3.pack(side=tkinter.TOP, anchor=tkinter.W)
    fractal_type_rad4.pack(side=tkinter.TOP, anchor=tkinter.W)

    # Выбор цвета
    color = "#000000"
    color_button = tkinter.Button(manage, text="Цвет")
    color_button.bind('<Button-1>', set_color)
    color_button.pack()

    # Ширина линии
    pen_width = tkinter.IntVar()
    pen_width.set(1)
    pen_width_scale = tkinter.Scale(manage, label="Толщина линии", orient=tkinter.HORIZONTAL, length=150, from_=1,
                                    to=10, tickinterval=1, resolution=1, variable=pen_width)
    pen_width_scale.pack()

    # Порядок фрактала
    fractal_power = tkinter.IntVar()
    fractal_power.set(0)  # по умолчанию это 0
    fractal_power_scale = tkinter.Scale(manage, label="Порядок кривой", orient=tkinter.HORIZONTAL, length=150, from_=0,
                                        to=20, tickinterval=5, resolution=1, variable=fractal_power)
    fractal_power_scale.pack()

    # Кнопка рисования
    draw_button = tkinter.Button(manage, text="Рисовать", width=12)
    draw_button.bind("<Button-1>", draw)
    draw_button.pack()

    # Кнопка стирания
    clear_button = tkinter.Button(manage, text="Стереть", width=12)
    clear_button.bind("<Button-1>", clear)
    clear_button.pack()

    root.mainloop()
