import tkinter
from tkinter.filedialog import asksaveasfilename

window = tkinter.Tk()
window.title('Вычисление объема сферы')
window.geometry('310x180')
window.resizable(False, False)


def calcul_sphere():
    try:
        radius = int(entry.get())
        result_txt.set(round(4 / 3 * 3.14 * (radius ** 3), 3))
    except:
        result_txt.set('Неверное значение')


def save_file():
    filepath = asksaveasfilename(
        defaultextension='txt',
        filetypes=[('Текстовый файл', '*.txt'), ("HTML файлы", "*.html")]
    )
    if filepath != '':
        text = str(eval(entry_result.get()))
        with open(filepath, 'w', encoding='UTF-8') as file:
            file.write(text)


label_input = tkinter.Label(window, text='Введите радиус:')
label_input.grid(row=0, column=0, sticky='w', padx=5)
label_result = tkinter.Label(window, text='Результат\nвычислений:', height=2)
label_result.grid(row=1, column=0, sticky='w', padx=5)

entry = tkinter.Entry(window)
entry.grid(row=0, column=1, pady=6, ipady=5)

result_txt = tkinter.StringVar()
entry_result = tkinter.Entry(window, textvariable=result_txt, state=tkinter.DISABLED)
entry_result.grid(row=1, column=1, pady=6, ipady=5)

btn = tkinter.Button(window, text='Вычислить', command=calcul_sphere)
btn.grid(row=2, columnspan=2, pady=5)

btn_save = tkinter.Button(window, text='Сохранить', command=save_file)
btn_save.grid(row=3, columnspan=2)

window.mainloop()
