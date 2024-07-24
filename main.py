from tkinter import Tk, Button, Frame, Entry
from func import *

button_gray = '#373737'
background_gray = '#2c2c2c'
lighter_gray = '#4f4f4f'
highlight_gray = '#181818'
darker_white = '#cecece'

def main():

    window = Tk()
    window.title("Calculator")
    window.minsize(288, 275)
    window.configure(background = background_gray)
    window.grid_columnconfigure(0, weight = 1)
    window.grid_rowconfigure(1, weight = 1)
    
    frame1 = Frame(window)
    frame1.configure(bg = background_gray)
    frame1.grid(sticky = 'nsew')
    frame1.grid_columnconfigure(0, weight = 1)

    frame2 = Frame(window)
    frame2.configure(bg = background_gray)
    frame2.grid(sticky = 'nsew')

    for n in range(4):
        frame2.grid_columnconfigure(n, weight = 1)

    for n in range(6):
        frame2.grid_rowconfigure(n, weight = 1)

    padding = 1
    thickness = 1

    entry_box = Entry(
        frame1,
        bg = '#272727', 
        fg = 'white', 
        font = ('Trebuchet', 16), 
        highlightthickness = thickness, 
        highlightbackground = highlight_gray,
        relief = 'flat', 
        )
    entry_box.grid(sticky = 'nsew', pady = padding)
    entry_box.config(cursor = 'xterm')

    Button(
        frame2, 
        bg = '#991121', 
        activebackground = '#b93638', 
        fg = 'white', 
        activeforeground = darker_white, 
        highlightbackground = highlight_gray,
        highlightthickness = thickness,
        relief = 'flat',
        text = '⌫', 
        font = ('Trebuchet', 14), 
        width = 3,
        command = lambda: clear_entry(entry_box)
        ).grid(row = 0, column = 0, padx = padding, pady = padding, sticky = 'nsew')

    Button(
        frame2, 
        bg = button_gray, 
        activebackground = lighter_gray, 
        fg = 'white', 
        activeforeground = darker_white, 
        highlightbackground = highlight_gray,
        highlightthickness = thickness,
        relief = 'flat',
        text = 'C', 
        font = ('Trebuchet', 14, 'bold'), 
        width = 3,
        command = lambda: entry_box.delete(0, END), 
        ).grid(row = 0, column = 1, padx = padding, pady = padding, sticky = 'nsew')
    

    pos_column = 2
    for n in ['(',')']:
        Button(
            frame2, 
            bg = button_gray, 
            activebackground = lighter_gray, 
            fg = 'white', 
            activeforeground = darker_white, 
            highlightbackground = highlight_gray,
            highlightthickness = thickness,
            relief = 'flat',
            text = n, 
            font = ('Trebuchet', 14), 
            width = 3,
            command = lambda n = n: add_character(n, entry_box), 
            ).grid(row = 0, column = pos_column, padx = padding, pady = padding, sticky = 'nsew')
        pos_column += 1
        
    pos_row = 1
    for n in ['+','-','/','*']:
        Button(
            frame2, 
            bg = '#b67000', 
            activebackground = '#ed9e23', 
            fg = 'white', 
            activeforeground = 'black', 
            highlightbackground = highlight_gray,
            highlightthickness = thickness,
            relief = 'flat',
            text = n, 
            font = ('Trebuchet', 14), 
            width = 3,
            command = lambda n = n: add_character(n, entry_box), 
            ).grid(row = pos_row, column = 3, padx = padding, pady = padding, sticky = 'nsew')
        pos_row += 1

    Button(
        frame2, 
        bg = button_gray, 
        activebackground = lighter_gray, 
        fg = 'white', 
        activeforeground = darker_white, 
        highlightbackground = highlight_gray, 
        highlightthickness = thickness, 
        relief = 'flat', 
        text = '.', 
        font = ('Trebuchet', 14), 
        width = 3, 
        command = lambda: add_character('.', entry_box), 
        ).grid(row = 4, column = 2, padx = padding, pady = padding, sticky = 'nsew')

    Button(
        frame2, 
        bg = button_gray, 
        activebackground = lighter_gray, 
        fg = 'white', 
        activeforeground = darker_white, 
        highlightbackground = highlight_gray, 
        highlightthickness = thickness, 
        relief = 'flat', 
        text = '%', 
        font = ('Trebuchet', 14), 
        width = 3, 
        command = lambda: add_character('%', entry_box), 
        ).grid(row = 4, column = 1, padx = padding, pady = padding, sticky = 'nsew')

    Button(
        frame2, 
        bg = button_gray, 
        activebackground = lighter_gray, 
        fg = 'white', 
        activeforeground = darker_white, 
        highlightbackground = highlight_gray, 
        highlightthickness = thickness, 
        relief = 'flat', 
        text = '√', 
        font = ('Trebuchet', 14), 
        width = 3, 
        command = lambda: add_character('√', entry_box), 
        ).grid(row = 5, column = 0, padx = padding, pady = padding, sticky = 'nsew')

    Button(
        frame2, 
        bg = button_gray, 
        activebackground = lighter_gray, 
        fg = 'white', 
        activeforeground = darker_white, 
        highlightbackground = highlight_gray, 
        highlightthickness = thickness, 
        relief = 'flat', 
        text = 'xʸ', 
        font = ('Trebuchet', 14), 
        width = 3, 
        command = lambda: add_character('^', entry_box), 
        ).grid(row = 5, column = 1, padx = padding, pady = padding, sticky = 'nsew')

    Button(
        frame2, 
        bg = '#0d761d', 
        activebackground = '#3d993e', 
        fg = 'white', 
        activeforeground = darker_white, 
        highlightbackground = highlight_gray, 
        highlightthickness = thickness, 
        relief = 'flat', 
        text = '=', 
        font = ('Trebuchet', 14),
        command = lambda: result(entry_box), 
        ).grid(row = 5, column = 2, padx = padding, pady = padding, sticky = 'nsew', columnspan=2)



        
    row_config = [(7,8,9), (4,5,6), (1,2,3), (0,)]
    # These tuples will provide a look more similar to a standard calculator and save some lines of code

    for x in row_config:
        for n in x:
            pos_column = n - x[0]
            pos_row  = row_config.index(x)
            Button(
                frame2, 
                bg = button_gray, 
                activebackground = lighter_gray, 
                fg = 'white', 
                activeforeground = darker_white, 
                highlightbackground = highlight_gray,
                highlightthickness = thickness,
                relief = 'flat',
                text = n, 
                font = ('Trebuchet', 14), 
                width = 3,
                command = lambda n = n: add_character(n, entry_box)
                ).grid(
                    row = pos_row + 1, 
                    column = pos_column, 
                    sticky = 'nsew', 
                    padx = padding, 
                    pady = padding, 
                    )

    









    window.mainloop()

main()