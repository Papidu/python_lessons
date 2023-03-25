import tkinter as tk

window = tk.Tk()


def button_clicked2(event):
    result_FIO = en1.get()
    result_course = en2.get()
    result_num = en3.get()
    label.configure(text=result_FIO + '\n' + result_course + '\n' + result_num)


def button_clicked():
    result_FIO = en1.get()
    result_course = en2.get()
    result_num = en3.get()
    label.configure(text=result_FIO + '\n' + result_course + '\n' + result_num)


label_FIO = tk.Label(text='Введите ваше ФИО:')
label_FIO.pack()

en1 = tk.Entry(width=20)
en1.pack()

label_course = tk.Label(text='Введите ваш курс:')
label_course.pack()

en2 = tk.Entry(width=20)
en2.pack()

label_num = tk.Label(text='Введите номер вашей группы:')
label_num.pack()

en3 = tk.Entry(width=20)
en3.pack()

button = tk.Button(text="ввод")
button.pack()
button.bind('<Return>', button_clicked2)
button.bind('<Button-1>', button_clicked2)

label = tk.Label()
label.pack()

window.mainloop()
