################################################################################
# Name of the project: ivs project 2
#
###############################################################################
#
# @file core
# @brief Core of the calculator. Reads the input and calculates the resoult. 
# 	
# At first, create grammar for the parser. Then parse input. Parser creates tree
# that is procesed and math functions are calculated in mathlib.py
#	
# @date 29.03.2023
#
# @author Matúš Hubinský
#
###############################################################################

import mathlib
import tkinter as tk

# The MIT License (MIT)
from lark import Lark, Transformer, v_args


###############################################################################
# authors: Sasank Chilamkurthy, Erez Shinan
# license: MIT
# edited code from github repository:
# https://github.com/lark-parser/lark/blob/master/examples/calc.py



# definicion of a grammar for parser
# TODO: sqrt()
grammar = """
	?start: sum
		  | NAME "=" sum    		-> assign_var
	?sum: product
		| sum "+" product   		-> add
		| sum "-" product   		-> sub
	?product: atom
 		| product "^" atom 			-> exp
		| product "*" atom  		-> mul
		| product "/" atom  		-> div
	?atom: NUMBER           		-> number
		| atom "$" atom 			-> root
		| atom "!"					-> fac 
		| "-" atom         			-> neg
		| NAME             			-> var
		| "(" sum ")"
	%import common.CNAME -> NAME
	%import common.NUMBER
	%import common.WS_INLINE
	%ignore WS_INLINE
"""


@v_args(inline=True)    # Affects the signatures of the methods
class CalculateTree(Transformer):
	from mathlib import add, sub, mul, div, fac, exp, neg, root
	number = float

	def __init__(self):
		self.vars = {}

	def assign_var(self, name, value):
		self.vars[name] = value
		return value

	def var(self, name):
		try:
			return self.vars[name]
		except KeyError:
			raise Exception("Variable not found: %s" % name)


# @author Matúš Hubinský, Sasank Chilamkurthy, Erez Shinan
# @brief procesing data from gui and calculating result
#  
# Create parser from Lark library. This parser is using grammar defined prieviously.
# Parser creates ASS that is procesed by CalculateTree() function. In this funcion,
# we are caling our math library named mathlib.py
# 
# @param data, input data from user 
def calculate(data) -> None:
	data = data.replace(chr(0x221A), '$')
	calc_parser = Lark(grammar, parser='lalr', transformer=CalculateTree())
	calc = calc_parser.parse
	print(calc(data))
	return calc(data)

###############################################################################
