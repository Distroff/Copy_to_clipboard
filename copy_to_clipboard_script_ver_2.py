import win32api, win32gui
import pyperclip
from datetime import date, timedelta, datetime
import locale
import time

from tkinter import *
from tkinter import ttk

flag = False
text = '---'
def get_data_from_entry():
    global flag, text
    inp_text = entry.get()
    show_name = inp_text.split('_')[1]
    show_date = datetime.strptime(inp_text.split('_')[-1], '%Y%m%d')

    #   Получаем день (числом), месяц (словом в родительном падеже) и год (числом)
    d = show_date.day
    m = genetive_converter(show_date)
    y = show_date.year

    #   Получаем день (числом), месяц (словом в родительном падеже) и год (числом)
    exp_date = date.today() + timedelta(days=7)
    exp_d = exp_date.day
    exp_m = genetive_converter(exp_date)
    exp_y = exp_date.year

    #   Формируем текст
    text = f'''Здравствуйте.
    
    Скачать спектакль "{show_name}" от {d} {m} {y} года можно по ссылке:
    
    
    Файл будет доступен до {exp_d} {exp_m} {exp_y} года.

    '''

    #   Копируем текст в буфер
    pyperclip.copy(text)
    finish_label.configure(text=text)  # сюда надо записать итоговый результат

    win.update()

    time.sleep(1)
    win.destroy()


def setCyrillicLayout():
    window_handle = win32gui.GetForegroundWindow()
    result = win32api.SendMessage(window_handle, 0x0050, 0, 0x04190419)
    return result


def setEngLayout():
    window_handle = win32gui.GetForegroundWindow()
    result = win32api.SendMessage(window_handle, 0x0050, 0, 0x04090409)
    return result


def genetive_converter(date_data: date) -> str:
    month_temp = date_data.strftime("%B").lower()
    month = month_temp[:-1] + 'я' if month_temp not in ('март', 'август') else month_temp + 'а'
    return month


def paste_fr_cl():
    # from_cb = pyperclip.paste()  # получаем текст из буфера обмена
    clipboard = win.clipboard_get()  # Get the copied item from system clipboard
    entry.insert('end', clipboard)  # Insert the item into the entry widget


#   Устанавливаем русскую локализацию
locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')

#   Переключаемся на русскую раскладку
setCyrillicLayout()


win = Tk()
win.title('Копируем текст письма в буфер обмена')

# Устанавливаем размеры окна
win.geometry("700x250")
entry_frame = Frame(win)  # widget Frame for entry line + button
entry_frame.pack()

#  Создаем виджет поле ввода
entry = Entry(entry_frame, width=42)

#  Initialize a Label widgets
text_for_entry = Label(entry_frame, text='Введите имя файла: ')
finish_label = Label(win, text=text, font=('Helvetica 13'))

#  Create Buttons widgets
btn_enter = ttk.Button(entry_frame, text="Enter", command=get_data_from_entry)  # To enter the input text
paste_from_cb = ttk.Button(win, text='Вставить из буфера обмена', command=paste_fr_cl)



# Drawing widgets
text_for_entry.pack(side=LEFT)
entry.pack(side=LEFT)
btn_enter.pack(side=LEFT)
paste_from_cb.pack()
finish_label.pack()

win.mainloop()


