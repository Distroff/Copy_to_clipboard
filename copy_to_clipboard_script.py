import pyperclip
from datetime import date, timedelta
import locale
import time

#   Устанавливаем русскую локализацию
locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')

#   Вводим данные
show_name = input('Введите название спектакля: >')
show_date = date.fromisoformat(input('Введите дату в формате YYYY-MM-DD: >'))

#   Получаем день (числом), месяц (словом в родительном падеже) и год (числом)
d = show_date.day
m = show_date.strftime("%B").lower()[:-1] + 'я'
y = show_date.year

#   Получаем день (числом), месяц (словом в родительном падеже) и год (числом)
exp_date = show_date + timedelta(days=7)
exp_d = exp_date.day
exp_m = exp_date.strftime('%B').lower()[:-1] + 'я'
exp_y = exp_date.year

#   Формируем текст
text = f'''Здравствуйте.

Скачать спектакль "{show_name}" от {d} {m} {y} года можно по ссылке:


Файл будет доступен до {exp_d} {exp_m} {exp_y} года.

'''

#   Копируем текст в буфер
pyperclip.copy(text)
pyperclip.paste()
print()
print(text)
time.sleep(1)