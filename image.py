from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('imagenes')

#imagen = Image.open('imgp.png')
#imagen.show()

img = ImageTk.PhotoImage(Image.open('imgp.png'))
l = Label(image=img)
l.pack()

root.mainloop()