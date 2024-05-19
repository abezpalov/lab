import random
from tkinter import *


# Создаём корневое окно
root = Tk()


# Тестовый обработчик событий
def but_command(event):
    print("Hey!")


# Тестовый обработчик событий
def clicked_command(event):
    print("I'm clicked")


# Кнопка и привязкой событий
but = Button(root, text="Нажми на меня")
but.bind("<Button-1>", clicked_command)
but.bind("<Button-3>", but_command)
but.pack()

# Метка для вывода текса


# Отображаем окно
root.mainloop()
