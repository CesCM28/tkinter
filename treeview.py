from tkinter import *
from tkinter import ttk

root = Tk()
root.title('hola mundo: treeview')

tree = ttk.Treeview(root)
tree['columns'] = ('Nombre', 'Telefono', 'Empresa')

# tree.column('#0')
tree.column('#0', width=0)
tree.column('Nombre')
tree.column('Telefono')
tree.column('Empresa')

# tree.heading('#0', text='id')
tree.heading('#0')
tree.heading('Nombre', text='Nombre')
tree.heading('Telefono', text='Telefono')
tree.heading('Empresa', text='Empresa')

tree.grid(column=0, row=0)

tree.insert('', END, 'lala', values=('Uno', 'Dos', 'Tres'), text='otro')
tree.insert('', END, 'lele', values=('cuetro', 'cinco', 'seis'), text='otro2')
tree.insert('lele', END, 'lolo', values=('ocho', 'nueve', 'diez'), text='otro3')

root.mainloop()