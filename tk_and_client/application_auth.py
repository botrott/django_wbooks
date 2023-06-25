import tkinter
from tkinter import ttk


def authorization():
    username = user_entry.get()
    password = password_entry.get()





window = tkinter.Tk()
window.title('AForm')
window.geometry('350x480')
window.resizable(False, False)


win = tkinter

main_label = tkinter.Label(window, text='Authorization')
main_label.pack()

logo = tkinter.PhotoImage(file='img/image1.png')
label = ttk.Label(image=logo)
label.pack()

user_label = tkinter.Label(window, text='name user', padx=1, pady=1)
user_label.pack()

user_entry = tkinter.Entry(window)
user_entry.pack()


user_password = tkinter.Label(window, text='password', padx=1, pady=1)
user_password.pack()

password_entry = tkinter.Entry(window)
password_entry.pack()

send_btn = tkinter.Button(window, text='Login', command=authorization)
send_btn.pack(padx=10, pady=8)



window.mainloop()
