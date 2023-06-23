import tkinter

window = tkinter.Tk()
window.geometry('310x150')
window.title('Temperature converter')

def convert_in_cels():
    try:
        t = eval(entry.get())
        tc = round(5 / 9 * (t - 32), 3)
        return label.config(text=str(tc))
    except (NameError, SyntaxError):
        return label.config(text='Введите число')


def convert_in_far():
    try:
        t = eval(entry.get())
        tf = round(9 / 5 * t + 32, 3)
        return label.config(text=str(tf))
    except (NameError, SyntaxError):
        return label.config(text='Введите число')


label = tkinter.Label(text='Temperature:')
label.pack()

frame = tkinter.Frame(window)
frame.pack()

entry = tkinter.Entry(frame)
entry.pack()

label = tkinter.Label(frame)
label.pack()

btn = tkinter.Button(frame, text='convert F to Celsius', command=convert_in_cels, padx=1, pady=8)
btn.pack(side=tkinter.LEFT)
btn2 = tkinter.Button(frame, text='convert C to Fahrenheit', command=convert_in_far, padx=1, pady=8)
btn2.pack(side=tkinter.RIGHT)

btn3 = tkinter.Button(text='Quit', command=window.destroy)
btn3.pack(padx=5, pady=8)

window.mainloop()
