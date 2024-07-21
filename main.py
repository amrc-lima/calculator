from tkinter import Tk, Entry, Button, Frame

vscode_gray = "#1f1f1f"
darker_gray = '#101010'
darker_white = '#cecece'

def main():
    window = Tk()
    window.title("Calculator")
    window.minsize(362,463)
    window.configure(background = vscode_gray)
    
    frame1 = Frame(window)
    frame1.configure(bg = vscode_gray)
    frame1.grid(column = 0, row = 0)

    frame2 = Frame(window)
    frame2.configure(bg = vscode_gray)
    frame2.grid(column = 0, row = 1)

    operation = Entry(
        frame1,
        bg = vscode_gray, 
        fg = 'white', 
        font = ('Trebuchet', 16), 
        highlightbackground = darker_white, 
        highlightthickness = 2,
        )
    operation.grid(sticky = 'ew')

    for n in range(10): 
        new_button = Button(
            frame2, 
            bg = vscode_gray, 
            activebackground = darker_gray, 
            fg = 'white', 
            activeforeground = darker_white, 
            text = n, 
            width = 5,
            )
        new_button.grid(row = (n//3), column = (n % 3), sticky = 'nsew')









    window.mainloop()

main()