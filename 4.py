import tkinter as tk

window = tk.Tk()
window.geometry('250x250')


def change_label_left(event):
    label['text'] = 'Левая кнопка мыши'


def change_label_right(event):
    label['text'] = 'Правая кнопка мыши'


def change_label_motion(event):
    x = event.x
    y = event.y
    label['text'] = "Движение мышью: {} x {}".format(x, y)


label = tk.Label(text="Щелкни мышкой")
label.pack()

window.bind('<Button-1>', change_label_left)
window.bind('<Button-3>', change_label_right)
window.bind('<Motion>', change_label_motion)

window.mainloop()
