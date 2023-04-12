################################################################################
# Name of the project: ivs project 2
#
###############################################################################
#
# @file test.py
# @brief Test for core.py and mathlib.py
#
# @date 02.04.2023
# @author Matúš Hubinský
#
###############################################################################


import core
import pytest
import mathlib


# TODO: test for priority
# @brief tests for the whole module calculate
# @param None
# @return None
def test_calculate() -> None:
	assert core.calculate("1+2") == 3
	assert core.calculate("1/2") == 0.5
	assert core.calculate("1000+2000") == 3000
	assert core.calculate("5*(5+5)") == 50
	assert core.calculate("2^10+1") == 1025


# @brief tests for function add() from mathlib
# @param None
# @return None
def test_addition() -> None:
	assert mathlib.add(None, 0, 0) == 0
	assert mathlib.add(None, 1, 2) == 3
	assert mathlib.add(None, -1, 1) == 0
	assert mathlib.add(None, 12345678901, 1) == 12345678902


# @brief tests for function sub() from mathlib
# @param None
# @return None
def test_substraction() -> None:
	assert mathlib.sub(None, 0, 0) == 0
	assert mathlib.sub(None, 1, 2) == -1
	assert mathlib.sub(None, 2, 1) == 1
	assert mathlib.sub(None, 1, 1) == 0
	assert mathlib.sub(None, -1, -1) == -2
	assert mathlib.sub(None, 12345678901, 1) == 12345678900


# @brief tests for function mul() from mathlib
# @param None
# @return None
def test_multiplication() -> None:
	assert mathlib.mul(None, 0, 0) == 0
	assert mathlib.mul(None, 1, 1) == 1
	assert mathlib.mul(None, 1, 2) == 2
	assert mathlib.mul(None, 2, 1) == 2
	assert mathlib.mul(None, 12345678901, 1) == 12345678901


# @brief tests for function div() from mathlib, divison by zero will return error
# @param None
# @return None
def test_divison() -> None:
	with pytest.raises(ZeroDivisionError):
		mathlib.div(None, 1, 0) == 0
	assert mathlib.div(None, 1, 1) == 1
	assert mathlib.div(None, 1, 2) == 0.5
	assert mathlib.div(None, 2, 1) == 2
	assert mathlib.div(None, 12345678901, 1) == 12345678901


# @brief tests for function fac() from mathlib, factorial from negative number is not defiend
# @param None
# @return None
def test_factorial() -> None:
	with pytest.raises(ValueError):
		mathlib.fac(None, -1) == 0
	assert mathlib.fac(None, 0) == 1
	assert mathlib.fac(None, 1) == 1
	assert mathlib.fac(None, 2) == 2
	assert mathlib.fac(None, 3) == 6
	assert mathlib.fac(None, 5) == 120
	assert mathlib.fac(
		None, 50) == 30414093201713378043612608166064768844377641568960512000000000000


# @brief tests for function exp() from mathlib
# @param None
# @return None
def test_exponentiationn() -> None:
	assert mathlib.exp(None, 0, 0) == 1
	assert mathlib.exp(None, 0, 1) == 0
	assert mathlib.exp(None, 2, 2) == 4
	assert mathlib.exp(None, 2, 10) == 1024
	assert mathlib.exp(None, -1, 1) == -1
	assert mathlib.exp(None, -1, 2) == 1
	assert mathlib.exp(None, -1, 10) == 1
	assert mathlib.exp(None, -1, 11) == -1


# @brief tests for function fac() from mathlib, factorial from negative number is not defiend
# @param None
# @return None
def test_nth_root() -> None:
	assert mathlib.root(None, 2, 0) == 0
	assert mathlib.root(None, 2, 1) == 1
	assert mathlib.root(None, 2, 2) == 1.4142135623730951
	assert mathlib.root(None, 10, 1024) == 2
	with pytest.raises(ValueError):
		mathlib.root(None, -1, 1)
		mathlib.root(None, -1, -2)

# @brief tests for function ln() from mathlib, natural logarithm from negative number is not defiend
# @param None
# @return None
def test_natural_logarithm() -> None:
	assert mathlib.ln(None, 1) == 0
	assert mathlib.ln(None, 2) == 0.693147
	assert mathlib.ln(None, 2.718281828459) == 1
	with pytest.raises(ValueError):
		mathlib.ln(None, -1)

### End of file test.py ###
