import tkinter as tk

window = tk.Tk()


def change():
    button['background'] = 'green'

def change1(e):
    button['background'] = 'green'

button = tk.Button(text='GUESS', width=10, height=3, command=change)
button.bind('<Motion>', change1)
button.pack()

window.mainloop()
