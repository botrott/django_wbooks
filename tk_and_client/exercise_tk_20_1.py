import tkinter

window = tkinter.Tk()
window.geometry('250x150')
window['bg'] = 'black'
window.title('Temperature converter')
window.resizable(False, False)

BACKGROUND = {'fg': 'lime', 'bg': 'black'}


def convert_in_cels():
    try:
        t = eval(entry.get())
        tc = round(5 / 9 * (t - 32), 3)
        return label.config(text=str(tc))
    except (NameError, SyntaxError):
        return label.config(text='Введите число', **BACKGROUND)


def convert_in_far():
    try:
        t = eval(entry.get())
        tf = round(9 / 5 * t + 32, 3)
        return label.config(text=str(tf))
    except (NameError, SyntaxError):
        return label.config(text='Введите число', **BACKGROUND)


label = tkinter.Label(text='Temperature:', **BACKGROUND)
label.pack()

frame = tkinter.Frame(window, bg='black')
frame.pack()

entry = tkinter.Entry(frame, **BACKGROUND)
entry.pack()

label = tkinter.Label(frame, **BACKGROUND)
label.pack()

btn = tkinter.Button(frame, text='convert F to C', command=convert_in_cels, padx=1, pady=8, **BACKGROUND)
btn.pack(side=tkinter.LEFT)
btn2 = tkinter.Button(frame, text='convert C to F', command=convert_in_far, padx=1, pady=8, **BACKGROUND)
btn2.pack(side=tkinter.RIGHT)

btn3 = tkinter.Button(text='Quit', command=window.destroy, **BACKGROUND)
btn3.pack(padx=5, pady=8)

window.mainloop()
