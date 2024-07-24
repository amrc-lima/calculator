from tkinter import INSERT, END
from re import sub

def add_character(character, entry_box):
    cursor_position = entry_box.index(INSERT)
    entry_box.insert(cursor_position, character)

def clear_entry(entry_box):
    cursor_position = entry_box.index(INSERT)
    if cursor_position > 0:
        entry_box.delete(cursor_position - 1)

def result(entry_box):
    entry_string  = entry_box.get()

    exponents = "⁰¹²³⁴⁵⁶⁷⁸⁹"
    numbers = "0123456789"

    for n in range(len(exponents)):
        if exponents[n] in entry_string:
            entry_string = sub(exponents[n], f"**{numbers[n]}", entry_string)
            print(entry_string)

    if "%" in entry_string:
        entry_string = sub('%', '/100 ', entry_string)

    if "^" in entry_string:
        entry_string = sub('\^', '**', entry_string)

    if "√" in entry_string:

        splitted_expression = entry_string.split('√')

        for n in range(len(splitted_expression)):
            splitted_expression[n] = splitted_expression[n].strip(" ")
            
        entry_string = splitted_expression[0]

        for part in splitted_expression[1:]:
            fin_idx = 0
            
            while fin_idx < len(part) and (part[fin_idx] in numbers or part[fin_idx] == '.'):
                fin_idx += 1
                
            part = " (" +  part[:fin_idx] + " ** 0.5)" + part[fin_idx:]
            entry_string += part
    
    entry_box.delete(0, END)

    try:
        entry_box.insert(0, eval(entry_string))
    except NameError:
        entry_box.insert(0, 'ERRO')
    except SyntaxError:
        entry_box.insert(0, 'ERRO')
    except TypeError:
        entry_box.insert(0, 'ERRO')