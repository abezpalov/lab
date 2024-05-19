"""
Лабораторная работа 5. Часть 1.

На форму поместите строку, кнопку и список с размерами шрифта.
Выбор размера шрифта в списке меняет на таковой размер текста в строке.
Нажатие на кнопку убирает одну букву из начала строки и добавляет ее в
конец строки, цвет текста строки при этом меняется случайным образом."""

import random
import tkinter

count = 0


def get_random_color():
    result = '#'
    for _ in range(6):
        result += hex(int(10000*random.random()) % 16)[-1]
    return result


def change_text_size(event):

    global label, listbox

    print("Запущен обработчик событий: change_text_size")
    print(f"{sizes[listbox.curselection()[0]]=}")
    label['font'] = ("Ubuntu", sizes[listbox.curselection()[0]])


def add_entropy(event):

    global label

    print("Запущен обработчик событий: add_entropy")
    label['text'] = label['text'][1:] + label['text'][0]
    label['foreground'] = get_random_color()

    global count
    count += 1

    # Добавим хаоса
    if count > 42:
        i = int(10000 * random.random()) % len(label['text'])
        label['text'] = label['text'][:i-1] + label['text'][i:]


def kill():
    exit()


if __name__ == "__main__":

    root = tkinter.Tk()
    root.title("Лабораторная 5a")
    root.geometry("1200x450")


    label = tkinter.Label(text="В замкнутой системе энтропия может только расти!")
    label.pack(anchor=tkinter.N, padx=20, pady=30)

    sizes = [12, 14, 16, 18, 20]
    listbox = tkinter.Listbox(listvariable=tkinter.Variable(value=sizes), selectmode=tkinter.SINGLE)
    listbox.pack(anchor=tkinter.CENTER, padx=20, pady=10)
    listbox.bind("<<ListboxSelect>>", change_text_size)

    button = tkinter.Button(text="Entropy++")
    button.pack(anchor=tkinter.S, padx=20, pady=10)
    button.bind("<Button-1>", add_entropy)



    root.mainloop()
