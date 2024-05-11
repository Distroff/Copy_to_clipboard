import win32api, win32gui
import pyperclip
from datetime import date, timedelta, datetime
import locale
import time



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

#   Устанавливаем русскую локализацию
locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')

#   Переключаемся на русскую раскладку
setCyrillicLayout()

#   Вводим данные
# show_name = input('Введите название спектакля: > ')
# show_date = date.fromisoformat(input('Введите дату в формате YYYY-MM-DD: > '))

show_filename = input('Введите название файла: > ')
show_name = show_filename.split('_')[1]
show_date = datetime.strptime(show_filename.split('_')[-1], '%Y%m%d')


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
t = pyperclip.paste()
# print(t)
print(text)
time.sleep(1)

# '''
# pyinstaller -F -i "C:\Users\JD\pypinst\Text.ico" copy_to_clipboard_script_2.py
# '''