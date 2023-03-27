##
# @file core.py
#
# @brief Calculating results from gui input
#

import tkinter as tk

##
# @brief Process the input stored in entry, call function to calculate the result and prints it back to entry
# @bug doesn't work yet
def calculate(entry) -> None:
	try:
		result = eval(entry.get())
		entry.delete(0, tk.END)
		entry.insert(tk.END, result)
	except:
		entry.delete(0, tk.END)
		entry.insert(tk.END, "Error")

# @brief calculate addition of two numbers
# @param a 
# @param b
# @return
def add(a, b) -> int:
	return a + b


# @brief calculate substract of two numbers
# @param a
# @param b
# @return 
def subtract(a, b) -> int:
	return a - b


# @brief multiply two numbers
# @param a
# @param b
# @return 
def multiply(a, b) -> int:
	return a * b


# @brief divade two numbers
# @param a
# @param b, can't be zero
# @return 
def divide(a, b) -> int:
	if (b == 0):
		print('Error: division by zero')
	return a / b


# @brief calculate resoult a to b power
# @param a
# @param b, exponent
# @return 
def exponent(a, b) -> None:
	return a ** b


# @brief calculate factorial of a number, factorial of 0 is 1
# @param a
# @return 
def factorial(a) -> None:
	# error handling
	if (a < 0):
		print("Error: can't calculate factorial of a negative number")	
 	# calculate factorial
	if ((a == 1) or (a == 0)):
		return 1
	return fac(a) * fac(a - 1)


# @brief calculate n rooth from nuber x
# @param x
# @param n
# @return 
def root(x, n) -> None:
	if (n < 0):
		print('Error: negative root is not defied')
	if ((x > 0) and (n%2 == 0)):
		print("Error: cant calculate odd root of negative number")
	return x**(1/n)
