from tkinter import *

root = Tk()
root.title('Pies a metros')

def calcular(*args):
    try:
        metros.set(int(0.3048 * float(pies.get()) * 10000 + 0.5) / 10000)
    except ValueError:
        metros.set('ERROR')


frame = Frame(root, pady=3, padx=12)
frame.grid(column=0, row=0)

pies = StringVar()
pies_input = Entry(frame, width=7, textvariable=pies)
pies_input.grid(column=1, row=0)

metros = StringVar()
metros.set('-')
Label(frame, textvariable=metros).grid(column=1, row=1)

Button(frame, text='Calcular', command=calcular).grid(column=2, row=2)

Label(frame, text='Pies').grid(column=0, row=0)
Label(frame, text='es igual a').grid(column=0, row=1)
Label(frame, text='metros').grid(column=2, row=1)

pies_input.focus()
root.bind("<Return>", calcular)

root.mainloop()