################################################################################
# Name of the project: ivs project 2
#
###############################################################################
#
# @file mathlib.py
# @brief library with all the math functions
#
# @date 02.04.2023
# @author Matúš Hubinský
#
###############################################################################


# @brief calculate addition of two numbers
# @param a
# @param b
# @return a plus b
def add(tree, a, b,) -> int:
	return a + b


# @brief calculate substract of two numbers
# @param a
# @param b
# @return a minus b
def sub(tree, a, b) -> int:
	if (a < 0 and b < 0):
		return -(abs(a) + abs(b))
	return a - b


# @brief multiply two numbers
# @param a
# @param b
# @return a multiplied by b
def mul(tree, a, b) -> int:
	return a * b


# @brief divade two numbers
# @param a
# @param b, can't be zero
# @return a divided by b
def div(tree, a, b) -> int:
	if (b == 0):
		raise ZeroDivisionError('Error: division by zero')
	return a / b


# @brief calculate resoult of a @a to @b power
# @param a, bae
# @param b, exponent
# @return a^b
def exp(tree, a, b) -> None:
	return a ** b


# @brief calculate factorial of a number, factorial of 0 is 1
# @param a
# @return factorial of a number
def fac(tree, a) -> None:
	# error handling
	if (a < 0):
		raise ValueError(
			"Error: can't calculate factorial of a negative number")
	# calculate factorial
	if ((a == 1) or (a == 0)):
		return 1
	return a * fac(None, a - 1)


# @brief calculate n rooth from number x
# @param x
# @param n
# @return n rooth from number x
def root(tree, n, x) -> None:
	if (x == 0 or x == 1):
		return x
	if (n == 1):
		raise ValueError('Error: root must be more than one')
	if (n < 0):
		raise ValueError('Error: negative root is not defiend')
	if ((x < 0) and (n % 2 == 0)):
		raise ValueError("Error: cant calculate odd root of negative number")
	return x**(1/n)


# @brief calculate negation of a
# @param a
# @return negation of number a  
def neg(tree, a) -> None:
	return -a


# @brief calculate a natural logarithm
# @param a
# @return natural logarithm of a rounded to 6 digits
def ln(tree, a):
	if a <= 0:
		raise ValueError(
			'Error: natural logaritm of a negative number is not defiend')
	n = 1000000.0
	return round(n * ((a ** (1/n)) - 1), 6)
