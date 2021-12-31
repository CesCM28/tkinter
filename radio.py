from tkinter import *

root = Tk()
root.title('radio')

PERSONAS = [
    ('Liz', 'amor'),
    ('Emma', 'amorx2'),
    ('Jacob', 'amorx3'),
    ('Santi', 'amorx4')
]

persona = StringVar()
persona.set('nada')

for text, valor in PERSONAS:
    Radiobutton(root, text=text, variable=persona, value=valor).pack()


l = Label(root, textvariable=persona).pack()

root.mainloop()