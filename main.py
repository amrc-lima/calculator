from tkinter import Tk, Label, Button

vscode_gray="#1f1f1f"
darker_gray='#101010'
darker_white='#cecece'

def main():
    window = Tk()
    window.title("Calculator")
    window.configure(background=vscode_gray)

    operation = Label(bg=vscode_gray)
    operation.pack(fill='x', expand=True)

    for n in range(10):
        new_button= Button(window, bg=vscode_gray, activebackground = darker_gray, fg = 'white', activeforeground =  darker_white, text=str(n))
        new_button.pack()








    window.mainloop()

main()