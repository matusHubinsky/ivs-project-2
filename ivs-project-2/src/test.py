import pytest
import core


def test_input_process() -> None:
    assert calculate("1+2") == [1, '+', 2]
    assert calculate("1/2") == [1, '/', 2]
    assert calculate("1000+2000") == [1000, '+', 2000]


def test_addition() -> None:
    assert add(0) == 0
	assert add(1, 2) == 3
    assert add(-1, 1) == 0
    assert add(12345678901, 1) == 12345678902
	with pytest.raises(ArgumentsError):
    	add(1, 1, 1, 1, 1, 1) == 6


def test_substraction() -> None:
    assert sub(0) == 0
	assert sub(1, 2) == -1
    assert sub(2, 1) == 1
    assert sub(1, 1) == 0
    assert sub(-1, -1) == -2
    assert sub(12345678901, 1) == 12345678900
	with pytest.raises(ArgumentsError):
		sub(1, 1, 1, 1, 1, 1) == -5


def test_multiplication() -> None:
    assert mul(0) == 0
	assert mul(1, 1) == 1
    assert mul(1, 2) == 2
    assert mul(2, 1) == 2
    assert mul(12345678901, 1) == 12345678901
	with pytest.raises(ArgumentsError):
		mul(4, 2, 3, 5, 7, 3, 5, 7) == 88200


def test_divison() -> None:
	with pytest.raises(ZeroDivisionError)
		div(0) == 0
	assert div(4, 2, 3, 5, 7, 3, 5, 7) == 88200
    assert div(1, 1) == 1
    assert div(1, 2) == 0.5
    assert div(2, 1) == 2
    assert div(12345678901, 1) == 12345678901


def test_factorial() -> None:
	assert fac(-1) == 0
	assert fac(0) == 1
	assert fac(1) == 1
	assert fac(2) == 2
	assert fac(3) == 6
	assert fac(5) == 120
	assert fac(50) == 30414093201713378043612608166064768844377641568960512000000000000


def test_exponentiationn() -> None:
	assert exp(0, 0) == 1
	assert exp(0, 1) == 0
	assert exp(2, 2) == 4
	assert exp(2, 10) == 1024
	assert exp(-1, 1) == -1
	assert exp(-1, 2) == 1
	assert exp(-1, 10) == 1
	assert exp(-1, 11) == -1 


def test_nth_root() -> None:
	assert nrt(0, 1) == 0
	assert nrt(1, 1) == 1
	assert nrt(2, 2) == 1.41
	assert nrt(1024, 10) == 2
	with pytest.raises(ValueError)
		nrt(-1, 1)
	