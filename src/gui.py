import os
from tkinter import *
import tkinter as tk
import core

# Create the main window
window = tk.Tk()
window.title("Softhorn Calculator")


# Define the function to move the window with cursor
def move_window(event):
    global x, y
    new_x = (window.winfo_x() - x) + event.x
    new_y = (window.winfo_y() - y) + event.y
    window.geometry(f"+{new_x}+{new_y}")

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
entry = tk.Entry(window, width=18, font=("Arial", 28), bg='grey90')
entry.grid(row=1, column=0, columnspan=4, padx=5, pady=20, ipady=25)

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
    
def on_enter_right(button):
    button.config(bg='#DCE9F2', fg='black')

def on_leave_right(button):
    button.config(bg='#898C96', fg='white')

def on_enter_top(button):
    button.config(bg='#DCE9F2', fg='black')

def on_leave_top(button):
    button.config(bg='#898C96', fg='white')

def calculate_result():
    tmp = core.calculate(entry.get())
    entry.delete(0, tk.END)
    entry.insert(tk.END, tmp)
    
# Create the buttons
button_1 = tk.Button(window, text="1", width=5, font=("Arial", 19), height=1, fg = 'white', bg='#898C96',
                     relief='ridge', bd=3, command=lambda: entry.insert(tk.END, "1"))
button_2 = tk.Button(window, text="2", width=5, font=("Arial", 19), height=1, fg = 'white', bg='#898C96',
                     relief='ridge', bd=3, command=lambda: entry.insert(tk.END, "2"))
button_3 = tk.Button(window, text="3", width=5, font=("Arial", 19), height=1, fg = 'white', bg='#898C96',
                     relief='ridge', bd=3, command=lambda: entry.insert(tk.END, "3"))
button_4 = tk.Button(window, text="4", width=5, font=("Arial", 19), height=1, fg = 'white', bg='#898C96',
                     relief='ridge', bd=3, command=lambda: entry.insert(tk.END, "4"))
button_5 = tk.Button(window, text="5", width=5, font=("Arial", 19), height=1, fg = 'white', bg='#898C96',
                     relief='ridge', bd=3, command=lambda: entry.insert(tk.END, "5"))
button_6 = tk.Button(window, text="6", width=5, font=("Arial", 19), height=1, fg = 'white', bg='#898C96',
                     relief='ridge', bd=3, command=lambda: entry.insert(tk.END, "6"))
button_7 = tk.Button(window, text="7", width=5, font=("Arial", 19), height=1, fg = 'white', bg='#898C96',
                     relief='ridge', bd=3, command=lambda: entry.insert(tk.END, "7"))
button_8 = tk.Button(window, text="8", width=5, font=("Arial", 19), height=1, fg = 'white', bg='#898C96',
                     relief='ridge', bd=3, command=lambda: entry.insert(tk.END, "8"))
button_9 = tk.Button(window, text="9", width=5, font=("Arial", 19), height=1, fg = 'white', bg='#898C96',
                     relief='ridge', bd=3, command=lambda: entry.insert(tk.END, "9"))
button_0 = tk.Button(window, text="0", width=5, font=("Arial", 19), height=1, fg = 'white', bg='#898C96',
                     relief='ridge', bd=3, command=lambda: entry.insert(tk.END, "0"))
button_plus = tk.Button(window, text="+", width=5, font=("Arial", 19), height=1, relief='ridge', fg = 'white',
                        bd=3, bg='#898C96', command=lambda: entry.insert(tk.END, "+"))
button_minus = tk.Button(window, text="-", width=5, height=1, relief='ridge', fg = 'white', font=("Arial", 19),
                         bd=3, bg='#898C96', command=lambda: entry.insert(tk.END, "-"))
button_multiply = tk.Button(window, text="*", width=5, font=("Arial", 19), height=1, relief='ridge', fg = 'white',
                            bd=3, bg='#898C96', command=lambda: entry.insert(tk.END, "*"))
button_divide = tk.Button(window, text="/", width=5, font=("Arial", 19), height=1, relief='ridge', fg = 'white',
                          bd=3, bg='#898C96', command=lambda: entry.insert(tk.END, "/"))
button_root = tk.Button(window, text=chr(0x221A), width=5, font=("Arial", 19), height=1, relief='ridge', fg = 'white',
                        bd=3, bg='#898C96', command=lambda: entry.insert(tk.END, chr(0x221A)))
button_power = tk.Button(window, text="pow", width=5, font=("Arial", 19), height=1, relief='ridge', fg = 'white',
                         bd=3, bg='#898C96', command=lambda: entry.insert(tk.END, "**"))
button_faktorial = tk.Button(window, text="!", width=5, height=1, relief='ridge', fg = 'white', font=("Arial", 19),
                             bd=3, bg='#898C96', command=lambda: entry.insert(tk.END, "!"))
button_neg = tk.Button(window, text="neg", width=5, fg = 'white', font=("Arial", 19),
                       height=1, relief='ridge', bd=3, bg='#898C96')
button_clear = tk.Button(window, text="C", width=5, font=("Arial", 19), height=1, relief='ridge', fg = 'white',
                         bd=3, bg='#A7CCFC', command=lambda: entry.delete(0, tk.END))
button_equal = tk.Button(window, text="=", width=5, fg = 'black', font=("Arial", 19),
                         height=1, relief='ridge', bd=3, bg='yellow', command=calculate_result)

# Add the buttons to the window\
button_root.grid(row=2, column=0)
button_power.grid(row=2, column=1)
button_faktorial.grid(row=2, column=2)
button_divide.grid(row=2, column=3)

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_plus.grid(row=3, column=3)

button_4.grid(row=4, column=0)
button_5.grid(row=4, column=1)
button_6.grid(row=4, column=2)
button_minus.grid(row=4, column=3)

button_7.grid(row=5, column=0)
button_8.grid(row=5, column=1)
button_9.grid(row=5, column=2)
button_multiply.grid(row=5, column=3)

button_neg.grid(row=6, column=0)
button_0.grid(row=6, column=1)
button_clear.grid(row=6, column=2)
button_equal.grid(row=6, column=3)

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

button_plus.bind("<Enter>", lambda event, button=button_plus: on_enter_right(button))
button_plus.bind("<Leave>", lambda event, button=button_plus: on_leave_right(button))

button_minus.bind("<Enter>", lambda event, button=button_minus: on_enter_right(button))
button_minus.bind("<Leave>", lambda event, button=button_minus: on_leave_right(button))

button_multiply.bind("<Enter>", lambda event, button=button_multiply: on_enter_right(button))
button_multiply.bind("<Leave>", lambda event, button=button_multiply: on_leave_right(button))

button_divide.bind("<Enter>", lambda event, button=button_divide: on_enter_right(button))
button_divide.bind("<Leave>", lambda event, button=button_divide: on_leave_right(button))

button_root.bind("<Enter>", lambda event, button=button_root: on_enter_top(button))
button_root.bind("<Leave>", lambda event, button=button_root: on_leave_top(button))

button_power.bind("<Enter>", lambda event, button=button_power: on_enter_top(button))
button_power.bind("<Leave>", lambda event, button=button_power: on_leave_top(button))

button_faktorial.bind("<Enter>", lambda event, button=button_faktorial: on_enter_top(button))
button_faktorial.bind("<Leave>", lambda event, button=button_faktorial: on_leave_top(button))

button_neg.bind("<Enter>", lambda event, button=button_neg: on_enter_top(button))
button_neg.bind("<Leave>", lambda event, button=button_neg: on_leave_top(button))

button_clear.bind("<Enter>", lambda event, button=button_clear: on_enter_c(button))
button_clear.bind("<Leave>", lambda event, button=button_clear: on_leave_c(button))

button_equal.bind("<Enter>", lambda event, button=button_equal: on_enter_equal(button))
button_equal.bind("<Leave>", lambda event, button=button_equal: on_leave_equal(button))


# Bind the function to the window so that it can be moved with the cursor
entry.bind("<Button-1>", start_drag)
entry.bind("<B1-Motion>", move_window)


window.mainloop()
