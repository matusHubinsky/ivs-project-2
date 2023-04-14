################################################################################
# Name of the project: ivs project 2
#
###############################################################################
#
# @file core.py
# @brief Core of the calculator. Reads the input and calculates the resoult. 
# 	
# At first, create grammar for the parser. Then parse input. Parser creates tree
# that is procesed and math functions are calculated in mathlib.py
#	
# @date 02.04.2023
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
# Copyright © 2017 Erez Shinan
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy of
# this software and associated documentation files (the "Software"), to deal in
# the Software without restriction, including without limitation the rights to
# use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
# the Software, and to permit persons to whom the Software is furnished to do so,
# subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
# FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.  IN NO EVENT SHALL THE AUTHORS OR
# COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
# IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
# CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


# definicion of a grammar for parser
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
		| "&" atom					-> ln 
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
	from mathlib import add, sub, mul, div, fac, exp, neg, root, ln
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
	data = data.replace("ln", '&')
	calc_parser = Lark(grammar, parser='lalr', transformer=CalculateTree())
	calc = calc_parser.parse
	print(calc(data))
	return calc(data)

###############################################################################
