from tkinter import *

root = Tk()
root.title('hola mundo!!')

root.geometry('500x500')

var = StringVar()
var.set('en el limbo')

def mostrar():
    l = Label(root, text=var.get())
    l.pack()


c = Checkbutton(root, text='Soy un checkbox', variable=var, onvalue='si', offvalue='nopo')
c.pack()

btn = Button(root, text='click', command=mostrar)
btn.pack()

root.mainloop()