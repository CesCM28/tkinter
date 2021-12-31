from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('hola mundo')

# def click():
#   messagebox.showwarning('Popup', 'Hola mundo!!')
# def click():
#    messagebox.showinfo('Popup', 'Hola mundo!!')
# def click():
#    messagebox.showerror('Popup', 'Hola mundo! :(')
#def click():
#    respuesta = messagebox.askquestion('Popup', 'Hola mundo??')
#    if respuesta == 'yes':
#        messagebox.showinfo('Respuesta', 'la respuesta fue ' + respuesta)
#    else:
#        messagebox.showwarning('Respuesta', 'la respuesta fue ' + respuesta)

#    print(respuesta)
#def click():
#    respuesta = messagebox.askokcancel('hola mundo', 'realizar acción?')
#    if respuesta:
#        messagebox.showinfo('Respuesta', 'la respuesta fue OK')
#    else:
#        messagebox.showwarning('Respuesta', 'la respuesta fue CANCEL')
    
#    print(respuesta)
def click():
    respuesta = messagebox.askyesno('hola mundo', 'realizar acción?')
    if respuesta:
        messagebox.showinfo('Respuesta', 'la respuesta fue YES')
    else:
        messagebox.showwarning('Respuesta', 'la respuesta fue NO')
    
    print(respuesta)


btn = Button(root, text='presioname', command=click)
btn.pack()

root.mainloop()
