from tkinter import *

root = Tk()

Entry(root).grid(row=0, column=0, columnspan=5)

Button(root, text='C').grid(row=1, column=0, sticky='w')
Button(root, text='CE').grid(row=1, column=1, sticky='w')

Button(root, text='0').grid(row=5, column=0)

columncount = 0

for x in range(1, 4):
    Button(root, text=str()).grid(row=4, column=columncount)
    columncount += 1

columncount = 0

for x in range(4, 7):
    Button(root, text=str(x)).grid(row=3, column=columncount)
    columncount += 1

columncount = 0

for x in range(7, 10):
    Button(root, text=str(x)).grid(row=2, column=columncount)
    columncount += 1

root.mainloop()