###############################################################################
# Name of the project: ivs project 2
#
###############################################################################
#
# @file gui.py
# @brief gui for the calculator
#
# @date 04.04.2023
# @author Adam Ďurica
#
###############################################################################

import os
from tkinter import *
from tkinter import messagebox
import core

# Create the main window
window = Tk()
window.title("Softhorn Calculator")

# Create a menu bar
menu_bar = Menu(window, background='#ADAEB3', relief='flat')

# Create a Help menu
help_menu = Menu(menu_bar, tearoff=0)
help_menu.add_command(label="About", command=lambda: messagebox.showinfo("About", "Softhorn Calculator\nVersion 1.0\n\nThis calculator was created by Softhorn team."))
help_menu.add_command(label="Commands", command=lambda: messagebox.showinfo("Commands", "Available commands:\n\n" + "\n".join(COMMANDS)))
menu_bar.add_cascade(label="Help", menu=help_menu)

# Display the menu bar
window.config(menu=menu_bar)

# Define the function to enable movement while draging the entry widget
def move_window(event):
    global x, y
    new_x = (window.winfo_x() - x) + event.x
    new_y = (window.winfo_y() - y) + event.y
    window.geometry(f"+{new_x}+{new_y}")

# Fuction to implement draging of the widget 
def start_drag(event):
    global x, y
    x, y = event.x, event.y

# Disable resizing of the window
window.resizable(False, False)

# Background color
window.config(bg='#ADAEB3')

# Use the os module to get the absolute path of the icon image file
icon_file = os.path.abspath('icon.png')
icon = PhotoImage(file=icon_file)
window.iconphoto(False, icon)

# Create an Entry widget to display the input and output
entry = Entry(window, width=19, font=("Arial", 28), bg='grey90', relief='flat')
entry.grid(row=1, column=0, columnspan=4, padx=5, pady=20, ipady=25)

# Creates the hover over button funtion that changes color of the button on entering
def on_enter(button):
    button.config(bg='#DCE9F2', fg='black')
def on_leave(button):
    button.config(bg='#898C96', fg='white')

def on_enter_c(button):
    button.config(bg='#DCE9F2', fg='black')
def on_leave_c(button):
    button.config(bg='#A7CCFC', fg='white')
    
def on_enter_equal(button):
    button.config(bg='white')
def on_leave_equal(button):
    button.config(bg='yellow')
    
def on_enter_backspace(button):
    button.config(bg='#DCE9F2', fg='black')
def on_leave_backspace(button):
    button.config(bg='#FF6347', fg='white')

###############################################################################
# Calls the funtion from core to calculate the result of inserted formula
def calculate_result():
    try:
        result = core.calculate(entry.get())
        entry.delete(0, END)
        entry.insert(END, str(result))
    except ValueError:
        messagebox.showerror("Error", "Invalid input!")

# Funtion that negates the FIRST inserted number
def negate_number():
    current_value = entry.get()
    if current_value.startswith('-'):
        entry.delete(0, 1)  # delete negative sign
    else:
        entry.insert(0, '-')  # insert negative sign

# Create the buttons
button_1 = Button(window, text="1", width=5, font=("Arial", 19), height=1, fg = 'white', bg='#898C96',
                     relief='flat', bd=3, command=lambda: entry.insert(END, "1"))
button_2 = Button(window, text="2", width=5, font=("Arial", 19), height=1, fg = 'white', bg='#898C96',
                     relief='flat', bd=3, command=lambda: entry.insert(END, "2"))
button_3 = Button(window, text="3", width=5, font=("Arial", 19), height=1, fg = 'white', bg='#898C96',
                     relief='flat', bd=3, command=lambda: entry.insert(END, "3"))
button_4 = Button(window, text="4", width=5, font=("Arial", 19), height=1, fg = 'white', bg='#898C96',
                     relief='flat', bd=3, command=lambda: entry.insert(END, "4"))
button_5 = Button(window, text="5", width=5, font=("Arial", 19), height=1, fg = 'white', bg='#898C96',
                     relief='flat', bd=3, command=lambda: entry.insert(END, "5"))
button_6 = Button(window, text="6", width=5, font=("Arial", 19), height=1, fg = 'white', bg='#898C96',
                     relief='flat', bd=3, command=lambda: entry.insert(END, "6"))
button_7 = Button(window, text="7", width=5, font=("Arial", 19), height=1, fg = 'white', bg='#898C96',
                     relief='flat', bd=3, command=lambda: entry.insert(END, "7"))
button_8 = Button(window, text="8", width=5, font=("Arial", 19), height=1, fg = 'white', bg='#898C96',
                     relief='flat', bd=3, command=lambda: entry.insert(END, "8"))
button_9 = Button(window, text="9", width=5, font=("Arial", 19), height=1, fg = 'white', bg='#898C96',
                     relief='flat', bd=3, command=lambda: entry.insert(END, "9"))
button_0 = Button(window, text="0", width=5, font=("Arial", 19), height=1, fg = 'white', bg='#898C96',
                     relief='flat', bd=3, command=lambda: entry.insert(END, "0"))
button_plus = Button(window, text="+", width=5, font=("Arial", 19), height=1, relief='flat', fg = 'white',
                        bd=3, bg='#898C96', command=lambda: entry.insert(END, "+"))
button_neg = Button(window, text="±", width=5, font=("Arial", 19), height=1, relief='flat', fg='white',
                        bd=3, bg='#898C96', command=negate_number)
button_minus = Button(window, text="-", width=5, height=1, relief='flat', fg = 'white', font=("Arial", 19),
                         bd=3, bg='#898C96', command=lambda: entry.insert(END, "-"))
button_multiply = Button(window, text="*", width=5, font=("Arial", 19), height=1, relief='flat', fg = 'white',
                            bd=3, bg='#898C96', command=lambda: entry.insert(END, "*"))
button_divide = Button(window, text="/", width=5, font=("Arial", 19), height=1, relief='flat', fg = 'white',
                          bd=3, bg='#898C96', command=lambda: entry.insert(END, "/"))
button_root = Button(window, text=chr(0x221A), width=5, font=("Arial", 19), height=1, relief='flat', fg = 'white',
                        bd=3, bg='#898C96', command=lambda: entry.insert(END, chr(0x221A)))
button_power = Button(window, text="x\u207F", width=5, font=("Arial", 19), height=1, relief='flat', fg = 'white',
                         bd=3, bg='#898C96', command=lambda: entry.insert(END, "^"))
button_faktorial = Button(window, text="!", width=5, height=1, relief='flat', fg = 'white', font=("Arial", 19),
                             bd=3, bg='#898C96', command=lambda: entry.insert(END, "!"))
button_clear = Button(window, text="C", width=5, font=("Arial", 19), height=1, relief='flat', fg = 'white',
                         bd=3, bg='#A7CCFC', command=lambda: entry.delete(0, END))
button_equal = Button(window, text="=", width=5, fg = 'black', font=("Arial", 19),
                         height=1, relief='flat', bd=3, bg='yellow', command=calculate_result)
button_left_bracket = Button(window, text="(", width=5, font=("Arial", 19), height=1, fg = 'white', bg='#898C96',
                     relief='flat', bd=3, command=lambda: entry.insert(END, "("))
button_rigth_bracket = Button(window, text=")", width=5, font=("Arial", 19), height=1, fg = 'white', bg='#898C96',
                     relief='flat', bd=3, command=lambda: entry.insert(END, ")"))
button_backspace = Button(window, text="⌫", width=5, font=("Arial", 19), height=1, fg='white', bg='#FF6347',
                     relief='flat', bd=3, command=lambda: entry.delete(len(entry.get())-1, END))
button_dot = Button(window, text=".", width=5, font=("Arial", 19), height=1, fg = 'white', bg='#898C96',
                     relief='flat', bd=3, command=lambda: entry.insert(END, "."))

# Add the buttons to the window
# First row of buttons
button_backspace.grid(row=2, column=0)
button_left_bracket.grid(row=2, column=1)
button_rigth_bracket.grid(row=2, column=2)
button_clear.grid(row=2, column=3)

# Second row of buttons
button_root.grid(row=3, column=0)
button_power.grid(row=3, column=1)
button_faktorial.grid(row=3, column=2)
button_divide.grid(row=3, column=3)

# Third row of buttons
button_1.grid(row=4, column=0)
button_2.grid(row=4, column=1)
button_3.grid(row=4, column=2)
button_plus.grid(row=4, column=3)

# Forth row of buttons
button_4.grid(row=5, column=0)
button_5.grid(row=5, column=1)
button_6.grid(row=5, column=2)
button_minus.grid(row=5, column=3)

# Fifth row of buttons
button_7.grid(row=6, column=0)
button_8.grid(row=6, column=1)
button_9.grid(row=6, column=2)
button_multiply.grid(row=6, column=3)

# Sixth row of buttons
button_neg.grid(row=7, column=0)
button_0.grid(row=7, column=1)
button_dot.grid(row=7, column=2)
button_equal.grid(row=7, column=3)

###############################################################################
# Bind the on_enter and on_leave funtions to buttons
button_1.bind("<Enter>", lambda event, button=button_1: on_enter(button))
button_1.bind("<Leave>", lambda event, button=button_1: on_leave(button))

button_2.bind("<Enter>", lambda event, button=button_2: on_enter(button))
button_2.bind("<Leave>", lambda event, button=button_2: on_leave(button))

button_3.bind("<Enter>", lambda event, button=button_3: on_enter(button))
button_3.bind("<Leave>", lambda event, button=button_3: on_leave(button))

button_4.bind("<Enter>", lambda event, button=button_4: on_enter(button))
button_4.bind("<Leave>", lambda event, button=button_4: on_leave(button))

button_5.bind("<Enter>", lambda event, button=button_5: on_enter(button))
button_5.bind("<Leave>", lambda event, button=button_5: on_leave(button))

button_6.bind("<Enter>", lambda event, button=button_6: on_enter(button))
button_6.bind("<Leave>", lambda event, button=button_6: on_leave(button))

button_7.bind("<Enter>", lambda event, button=button_7: on_enter(button))
button_7.bind("<Leave>", lambda event, button=button_7: on_leave(button))

button_8.bind("<Enter>", lambda event, button=button_8: on_enter(button))
button_8.bind("<Leave>", lambda event, button=button_8: on_leave(button))

button_9.bind("<Enter>", lambda event, button=button_9: on_enter(button))
button_9.bind("<Leave>", lambda event, button=button_9: on_leave(button))

button_0.bind("<Enter>", lambda event, button=button_0: on_enter(button))
button_0.bind("<Leave>", lambda event, button=button_0: on_leave(button))

button_plus.bind("<Enter>", lambda event, button=button_plus: on_enter(button))
button_plus.bind("<Leave>", lambda event, button=button_plus: on_leave(button))

button_minus.bind("<Enter>", lambda event, button=button_minus: on_enter(button))
button_minus.bind("<Leave>", lambda event, button=button_minus: on_leave(button))

button_multiply.bind("<Enter>", lambda event, button=button_multiply: on_enter(button))
button_multiply.bind("<Leave>", lambda event, button=button_multiply: on_leave(button))

button_divide.bind("<Enter>", lambda event, button=button_divide: on_enter(button))
button_divide.bind("<Leave>", lambda event, button=button_divide: on_leave(button))

button_root.bind("<Enter>", lambda event, button=button_root: on_enter(button))
button_root.bind("<Leave>", lambda event, button=button_root: on_leave(button))

button_power.bind("<Enter>", lambda event, button=button_power: on_enter(button))
button_power.bind("<Leave>", lambda event, button=button_power: on_leave(button))

button_faktorial.bind("<Enter>", lambda event, button=button_faktorial: on_enter(button))
button_faktorial.bind("<Leave>", lambda event, button=button_faktorial: on_leave(button))

button_neg.bind("<Enter>", lambda event, button=button_neg: on_enter(button))
button_neg.bind("<Leave>", lambda event, button=button_neg: on_leave(button))

button_clear.bind("<Enter>", lambda event, button=button_clear: on_enter_c(button))
button_clear.bind("<Leave>", lambda event, button=button_clear: on_leave_c(button))

button_equal.bind("<Enter>", lambda event, button=button_equal: on_enter_equal(button))
button_equal.bind("<Leave>", lambda event, button=button_equal: on_leave_equal(button))

button_left_bracket.bind("<Enter>", lambda event, button=button_left_bracket: on_enter(button))
button_left_bracket.bind("<Leave>", lambda event, button=button_left_bracket: on_leave(button))

button_rigth_bracket.bind("<Enter>", lambda event, button=button_rigth_bracket: on_enter(button))
button_rigth_bracket.bind("<Leave>", lambda event, button=button_rigth_bracket: on_leave(button))

button_backspace.bind("<Enter>", lambda event, button=button_backspace: on_enter_backspace(button))
button_backspace.bind("<Leave>", lambda event, button=button_backspace: on_leave_backspace(button))

button_dot.bind("<Enter>", lambda event, button=button_dot: on_enter(button))
button_dot.bind("<Leave>", lambda event, button=button_dot: on_leave(button))

###############################################################################
# Define the commands available in the calculator
COMMANDS = [    "1 ~ Inserts number 1", "2 ~ Inserts number 2", "3 ~ Inserts number 3", "4 ~ Inserts number 4",
                "5 ~ Inserts number 5", "6 ~ Inserts number 6", "7 ~ Inserts number 7", "8 ~ Inserts number 8",
                "9 ~ Inserts number 9", "0 ~ Inserts number 0", "+ ~ Inserts sign +",
                "- ~ Inserts sign -", "* ~ Inserts sign *", "/ ~ Inserts sign /", chr(0x221A)+
                " ~ Insert the number for root then insert the degree of the root", 'x\u207F ~ Insert number raised to the power n',
                "! ~ Calculates the factorial of the inserted number", "C ~ Clears the inserted numbers and signes",
                "⌫ ~ Deletes the last inserted character", "( ~ Inserts left bracket", ") ~ Inserts right bracket", 
                "± ~ Negates the FISRT inserted number", "= ~ Calculates the result"]

# Bind the function to the entry widget so that it can be moved with the cursor
entry.bind("<Button-1>", start_drag)
entry.bind("<B1-Motion>", move_window)

# Bind the enter key to calculate result
window.bind('<Return>', lambda event: calculate_result())

window.mainloop()