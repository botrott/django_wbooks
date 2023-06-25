import tkinter
from tkinter import ttk
from tkinter import messagebox
import sqlite3

con = sqlite3.connect('userdata.db')
cur = con.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS users
                (username TEXT PRIMARY KEY,
                password TEXT,
                gender TEXT)
            ''')
con.commit()

GENDER_LST = ['man', 'woman']


def register():
    def register_verification():
        username = username_entry.get()
        password = password_entry.get()
        gender = gender_m.get()
        if username != '' and password != '':
            result = (username, password, gender)
            try:
                con = sqlite3.connect('userdata.db')
                cur = con.cursor()
                cur.execute('INSERT INTO users VALUES (?, ?, ?)', result)
                con.commit()
                messagebox.showinfo('OK', f'Пользователь: {username}\nуспешно добавлен')
            except Exception as err:
                messagebox.showerror('', err)
        else:
            messagebox.showerror('NOK', 'Заполните все поля!')

    register_s = tkinter.Toplevel(window)
    register_s.title('Регистрация')
    register_s.geometry('260x270')
    register_s.resizable(False, False)
    register_s.grab_set()

    username = tkinter.StringVar()
    password = tkinter.StringVar()

    tkinter.Label(register_s, text='Заполните поля').pack()
    tkinter.Label(register_s, text='').pack()

    username_lable = tkinter.Label(register_s, text='Имя * ')
    username_lable.pack()

    username_entry = tkinter.Entry(register_s, textvariable=username)
    username_entry.pack()

    password_lable = tkinter.Label(register_s, text='Пароль * ')
    password_lable.pack()

    password_entry = tkinter.Entry(register_s, textvariable=password)
    password_entry.pack()

    gender_m = tkinter.StringVar(register_s, value=GENDER_LST[0])

    f_top = tkinter.LabelFrame(register_s, text='Пол')
    f_top.pack(pady=5)
    btn = ttk.Radiobutton(f_top, text='муж', value=GENDER_LST[0], variable=gender_m)
    btn.pack(side=tkinter.LEFT)
    btn2 = ttk.Radiobutton(f_top, text='жен', value=GENDER_LST[1], variable=gender_m)
    btn2.pack(side=tkinter.LEFT)

    tkinter.Button(register_s, text='Регистрация', relief=tkinter.SOLID, cursor='hand2',
                   command=register_verification).pack(pady=15)


def login():
    def login_verification():
        username_enter = username_entry.get()
        password_enter = password_entry.get()
        try:
            con = sqlite3.connect('userdata.db')
            cur = con.cursor()
            cur.execute("SELECT username, password FROM users")
            for row in cur.fetchall():
                if username_enter in row and password_enter == row[1]:
                    messagebox.showinfo('OK', 'Доступ разрешен')
                    break
            else:
                messagebox.showerror('NOK', 'Неверный логин или пароль')

        except Exception as err:
            messagebox.showerror('', err)

    register_s = tkinter.Toplevel(window)
    register_s.title('Login')
    register_s.geometry('260x200')
    register_s.grab_set()

    username = tkinter.StringVar()
    password = tkinter.StringVar()

    tkinter.Label(register_s, text='Введите свое имя и пароль').pack()
    tkinter.Label(register_s, text='').pack()

    username_lable = tkinter.Label(register_s, text='Имя * ')
    username_lable.pack()

    username_entry = tkinter.Entry(register_s, textvariable=username)
    username_entry.pack()

    password_lable = tkinter.Label(register_s, text='Пароль * ')
    password_lable.pack()

    password_entry = tkinter.Entry(register_s, textvariable=password)
    password_entry.pack()

    tkinter.Button(register_s, text='Войти', padx=5, pady=5, command=login_verification).pack(padx=10, pady=8)


window = tkinter.Tk()
window.title('AForm')
window.geometry('350x430')
window.resizable(False, False)
window.eval('tk::PlaceWindow . center')

logo = tkinter.PhotoImage(file='img/image1.png')
label = ttk.Label(image=logo)
label.pack()

main_label = tkinter.Label(window, text='Выберите свой вариант')
main_label.pack()

login_btn = tkinter.Button(window, text='Войти', command=login)
login_btn.pack(padx=10, pady=8, ipadx=15, ipady=1)

register_btn = tkinter.Button(window, text='Регистрация', command=register)
register_btn.pack(padx=10, pady=8, ipadx=5, ipady=1)

window.mainloop()
