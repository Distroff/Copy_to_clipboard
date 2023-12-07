import win32api, win32gui
import pyperclip
from datetime import date, timedelta
import locale
import time



import tkinter as tk

def say_hello():
    '''

    :return: Hello!
    '''
    print('Hello!')

def add_label():
    '''

    :return: click => label
    '''
    label = tk.Label(win, text=f'label', foreground='green')
    label.pack()

def counter():
    '''
    считаем нажатие кнопки 4
    :return:
    '''
    global btn4_count
    btn4_count += 1
    btn4['text'] = f'Кнопка4 счетчик{btn4_count}'


win = tk.Tk()
win.title('Копируем текст в буфер обмена')  # название окна
win.geometry('600x600+100+100')     # размер окна
win.resizable(True, True)   # возможность изменения размера
win.minsize(800, 800)   # минимальный размер
win.maxsize(1000, 1000) # максимальный размер
logo = tk.PhotoImage(file='files/copy.png')
win.iconphoto(False, logo)
win.config(background='gray')

# label_1 = tk.Label(win, text='Hello',
#                    bg='darkgray',
#                    fg='red',
#                    font=('Calibri', 20, 'bold'),
#                    width=10,
#                    relief=tk.RAISED,
#                    bd=5,
#                    )
# label_1.pack()



btn1 = tk.Button(win, text='Кнопка1',
                 command=say_hello,
                 state=tk.DISABLED
                 )
btn2 = tk.Button(win, text='Кнопка2',
                 command=add_label)

btn3 = tk.Button(win, text='Кнопка3',
                 command=lambda: tk.Label(win, text='lambda button3').pack()
                 )
btn4_count = 0
btn4 = tk.Button(win, text=f'Кнопка4 счетчик{btn4_count}',
                 command=counter,
                 activebackground='red',
                 bg='blue'
                 )

btn1.pack()
btn2.pack()
btn3.pack()
btn4.pack()




win.mainloop()








'''
сюда вставить код из copy_to_clipboard_script_2.py
'''