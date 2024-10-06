import win32api, win32gui
import pyperclip
from datetime import date, timedelta, datetime
import locale
import time
import subprocess
import webbrowser
import os

from tkinter import *




flag = False
final_text = '---'


def open_browsers(file_name):
    upload_url = 'f.gamt.su'
    webbrowser.open(upload_url)  # открываем страницу для загрузки файла
    file_path = ''
    id_n = file_name.split('_')[0]  # получаем id номер файла
    start_path = fr'V:\DATA\{id_n[2]}\{id_n[1]}\{id_n[0]}'
    file_list = os.listdir(start_path)  # список файлов в папке
    for f_n in file_list:
        if f_n.startswith(id_n):
            file_path = fr'{start_path}\{f_n}'
            break

    explorer_on_file(file_path)  # открываем проводник с файлом
    # print(file_path)


def get_data_from_entry():
    global flag, final_text
    inp_text = filename_entry.get()
    id_show, show_name, show_date_str = inp_text.split('_')
    show_date = datetime.strptime(show_date_str, '%Y%m%d')

    #   Получаем день (числом), месяц (словом в родительном падеже) и год (числом)
    d = show_date.day
    m = genetive_converter(show_date)
    y = show_date.year

    #   Получаем день (числом), месяц (словом в родительном падеже) и год (числом)
    exp_date = date.today() + timedelta(days=7)
    exp_d = exp_date.day
    exp_m = genetive_converter(exp_date)
    exp_y = exp_date.year




    #   ОТКРЫВАЕМ ТЕСТ БРАУЗЕР И ИЩЕМ EMAIL АДРЕСАТА, УЗНАЕМ ИНИЦИАЛЫ

    first_name = ''
    patron_name = ''
    last_name = ''
    email = 'addres@mariinsky.ru'

    #   ОТКРЫВАЕМ НОВУЮ ВКЛАДКУ, ЗАПУСКАЕМ ЗАГРУЗКУ ФАЙЛА И ЖДЕМ ССЫЛКУ

    link_for_download = ''

    #   Формируем текст
    final_text = f'''Здравствуйте, {first_name} {patron_name}!

    Скачать спектакль "{show_name}" от {d} {m} {y} года можно по ссылке:

    {link_for_download}

    Файл будет доступен до {exp_d} {exp_m} {exp_y} года.
    
    {email}
    '''

    #   Копируем текст в буфер
    pyperclip.copy(final_text)
    finish_label.configure(text=final_text)  # сюда надо записать итоговый результат

    win.update()

    time.sleep(1)
    open_browsers(inp_text)  # ищем путь к файлу запускаем проводник и браузер
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
    filename_entry.insert('end', clipboard)  # Insert the item into the entry widget


def explorer_on_file(url):
    """ opens a Windows explorer window """
    subprocess.Popen(fr'explorer /select,"{url}"')

def check_correct_name(filename:str) -> bool:
    '''Сделать проверку на правильность файла'''
    pass

# ============= MAIN CODE =============

#   Устанавливаем русскую локализацию
locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')

#   Переключаемся на русскую раскладку
# setCyrillicLayout()

win = Tk()
win.title('Копируем текст письма в буфер обмена')

# Устанавливаем размеры окна
win.geometry("1000x250")
entry_filename_frame = Frame(win,
                        padx=10,
                        pady=10) # borderwidth=2, background='grey')  # widget Frame название файла и кнопка
entry_filename_frame.pack()
entry_fio_frame = Frame(win,
                        padx=10,
                        pady=10)  # widget фамилия
entry_fio_frame.pack()

#  Создаем виджет поле ввода


#  Initialize a Label widgets
label_for_filename_entry = Label(entry_filename_frame,
                                 text='Введите имя файла: ')    # padx=10, pady=10, font=('Helvetica 11'))
fio_label = Label(entry_fio_frame,
                  text="Введите фамилию (опционально): ",
                  font=('Helvetica 12'))
finish_label = Label(win,
                     text=final_text,
                     font=('Helvetica 13', 15, 'bold'))

#  Create Buttons widgets
btn_enter = Button(win, text="GO!",
                   command=get_data_from_entry,
                   padx=10,
                   pady=10,
                   height=3,
                   width=10)  # To enter the input text
paste_from_cb_button = Button(entry_filename_frame,
                              text='Вставить название из буфера обмена =>> ',
                              font=('Helvetica 12'),
                              background='lightgrey',
                              activebackground='lightyellow',
                              command=paste_fr_cl)

# Create entry fields
filename_entry = Entry(entry_filename_frame,
                       width=42, )
fio_entry = Entry(entry_fio_frame,
                  width=42)

# Drawing widgets

# label_for_filename_entry.pack(side=LEFT)  # Поле "Введите название файла"
paste_from_cb_button.pack(side=LEFT)  # кнопка вставить из буфера
filename_entry.pack(side=LEFT)  #  Поле для ввода названия файла

fio_label.pack(side=LEFT)
fio_entry.pack()

btn_enter.pack()

finish_label.pack()

win.mainloop()


