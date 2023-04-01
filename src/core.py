##
# @file core.py
#
# @brief Calculating results from gui input
#

import tkinter as tk


##
# @brief Process the input stored in entry, call function to calculate the result and prints it back to entry
# @bug doesn't work yet
def calculate(gui_input) -> None:
	return eval(gui_input)


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
def sub(a, b) -> int:
	return a - b


# @brief multiply two numbers
# @param a
# @param b
# @return 
def mul(a, b) -> int:
	return a * b


# @brief divade two numbers
# @param a
# @param b, can't be zero
# @return 
def div(a, b) -> int:
	if (b == 0):
		raise ZeroDivisionError('Error: division by zero')
	return a / b


# @brief calculate resoult a to b power
# @param a
# @param b, exponent
# @return 
def exp(a, b) -> None:
	return a ** b


# @brief calculate factorial of a number, factorial of 0 is 1
# @param a
# @return 
def fac(a) -> None:
	# error handling
	if (a < 0):
		raise ValueError("Error: can't calculate factorial of a negative number")	
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
		raise ValueError('Error: negative root is not defied')
	if ((x < 0) and (n%2 == 0)):
		raise ValueError("Error: cant calculate odd root of negative number")
	return x**(1/n)
