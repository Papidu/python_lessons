import tkinter as tk

window = tk.Tk()


def change_color1(event):
    button['background'] = 'sky blue'
    button['text'] = 'PINK/BLUE'

def change_color2(event):
    button['background'] = 'pink'
    button['text'] = 'Нажмите Enter'


button = tk.Button(text='PINK/BLUE')
button.bind('<Button-3>', change_color2)
button.bind('<Button-1>', change_color1)

button.pack()

window.mainloop()
