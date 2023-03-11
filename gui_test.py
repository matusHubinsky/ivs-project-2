import tkinter as tk

# Function to calculate the result
def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Create the main window
window = tk.Tk()
window.title("Calculator")

# Create an Entry widget to display the input and output
entry = tk.Entry(window, width=30, font=("Arial", 14))
entry.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

# Create the buttons
button_1 = tk.Button(window, text="1", width=5, height=2, relief='raised', bd=5, highlightthickness=0, command=lambda: entry.insert(tk.END, "1"))
button_2 = tk.Button(window, text="2", width=5, height=2, relief='raised', bd=3, command=lambda: entry.insert(tk.END, "2"))
button_3 = tk.Button(window, text="3", width=5, height=2, relief='raised', bd=3, command=lambda: entry.insert(tk.END, "3"))
button_4 = tk.Button(window, text="4", width=5, height=2, relief='raised', bd=3, command=lambda: entry.insert(tk.END, "4"))
button_5 = tk.Button(window, text="5", width=5, height=2, relief='raised', bd=3, command=lambda: entry.insert(tk.END, "5"))
button_6 = tk.Button(window, text="6", width=5, height=2, relief='raised', bd=3, command=lambda: entry.insert(tk.END, "6"))
button_7 = tk.Button(window, text="7", width=5, height=2, relief='raised', bd=3, command=lambda: entry.insert(tk.END, "7"))
button_8 = tk.Button(window, text="8", width=5, height=2, relief='raised', bd=3, command=lambda: entry.insert(tk.END, "8"))
button_9 = tk.Button(window, text="9", width=5, height=2, relief='raised', bd=3, command=lambda: entry.insert(tk.END, "9"))
button_0 = tk.Button(window, text="0", width=5, height=2, relief='raised', bd=3, command=lambda: entry.insert(tk.END, "0"))
button_plus = tk.Button(window, text="+", width=5, height=2, relief='raised', bd=3, bg='DarkGoldenrod1', command=lambda: entry.insert(tk.END, "+"))
button_minus = tk.Button(window, text="-", width=5, height=2, relief='raised', bd=3, bg='DarkGoldenrod1', command=lambda: entry.insert(tk.END, "-"))
button_multiply = tk.Button(window, text="*", width=5, height=2, relief='raised', bd=3, bg='DarkGoldenrod1', command=lambda: entry.insert(tk.END, "*"))
button_divide = tk.Button(window, text="/", width=5, height=2, relief='raised', bd=3, bg='DarkGoldenrod1', command=lambda: entry.insert(tk.END, "/"))
button_clear = tk.Button(window, text="C", width=5, height=2, relief='raised', bd=3, bg='DarkGoldenrod1', command=lambda: entry.delete(0, tk.END))
button_equal = tk.Button(window, text="=", width=5, height=2, relief='raised', bd=3, bg='yellow', command=calculate)

# Add the buttons to the window
button_1.grid(row=1, column=0)
button_2.grid(row=1, column=1)
button_3.grid(row=1, column=2)
button_plus.grid(row=1, column=3)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_minus.grid(row=2, column=3)

button_7.grid(row=3, column=0)
button_8.grid(row=3, column=1)
button_9.grid(row=3, column=2)
button_multiply.grid(row=3, column=3)

button_clear.grid(row=4, column=0)
button_0.grid(row=4, column=1)
button_divide.grid(row=4, column=2)
button_equal.grid(row=4, column=3)

def add():
    try:
        nums = entry.get().split("+")
        result = sum([float(num.strip()) for num in nums])
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def subtract():
    try:
        nums = entry.get().split("-")
        result = float(nums[0].strip()) - sum([float(num.strip()) for num in nums[1:]])
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def multiply():
    try:
        nums = entry.get().split("*")
        result = 1
        for num in nums:
            result *= float(num.strip())
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def divide():
    try:
        nums = entry.get().split("/")
        result = float(nums[0].strip())
        for num in nums[1:]:
            result /= float(num.strip())
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

root = tk.Tk()
root.mainloop()