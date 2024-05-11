#  Import the required libraries

from tkinter import *
from tkinter import ttk


win = Tk()
win.title('Копируем текст письма в буфер обмена')

# Устанавливаем размеры окна
win.geometry("700x250")
entry_frame = Frame(win)
entry_frame.pack()


def get_data_from_entry():
    inp_text = entry.get()
    finish_label.configure(text=inp_text)  # сюда надо записать итоговый результат
    print(inp_text)


def paste_fr_cl():
    # from_cb =  # получаем текст из буфера обмена
    pass


#  Создаем виджет поле ввода
entry = Entry(entry_frame, width=42)

#  Initialize a Label widgets
text_for_entry = Label(entry_frame, text='Введите имя файла: ')
finish_label = Label(win, text="---", font=('Helvetica 13'))


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







'''
сюда вставить код из copy_to_clipboard_script_2.py
'''