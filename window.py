from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('hola mundo!!')

# solucion #1
#def open():
#    img = ImageTk.PhotoImage(Image.open('images/1.png'))
#    top = Toplevel()
#    top.title('hola ventana!!')
#    l1 = Label(top, text='es una ventana nueva!!')
#    l2 = Label(top, image=img)
#    l1.pack()
#    l2.pack()
#    top.mainloop()

# solucion #2
#def open():
#    global img
#    img = ImageTk.PhotoImage(Image.open('images/2.png'))
#    top = Toplevel()
#    top.title('hola ventana!!')
#    l1 = Label(top, text='es una ventana nueva!!')
#    l2 = Label(top, image=img)
#    l1.pack()
#    l2.pack()

# solucion #3 
def open(img):
    top = Toplevel()
    top.title('hola ventana!!')
    l1 = Label(top, text='es una ventana nueva!!')
    l2 = Label(top, image=img)
    l1.pack()
    l2.pack()


img = ImageTk.PhotoImage(Image.open('images/3.png')) #sol 3
btn = Button(root, text='Click', command=lambda: open(img)).pack()
#btn = Button(root, text='Click', command=open).pack() #sol 1 y 2
root.mainloop()