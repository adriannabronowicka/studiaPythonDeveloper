"""
5! 1x2x3x4x5
0! 1
-1! nie istnieje
"""
import pytest


class OutOfRangeError(Exception):
    ...


def factorial(n: int):
    if n < 0:
        raise OutOfRangeError
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

from functools import reduce
from operator import mul


def fancy_factorial(m: int):
    return reduce(mul, range(1, n+1))


@pytest.mark.parametrize("factorial_input, expected_output",
                         [
                             (3, 6),
                             (5, 120),
                             (0, 1),
                             (1, 1),
                             (10, 3628800)
                         ]
                         )
def test_factorial(factorial_input: int, expected_output: int):
   result = factorial(factorial_input)
   assert result == expected_output

"""
def test_factorial_1():
   result = factorial(0)
   assert result == 1


def test_factorial_2():
    result = factorial(1)
    assert result == 1


def test_factorial_3():
    result = factorial(1)
    assert result == 1"""


"""def test_factorial_4():
    try:
        factorial(-1)
    except OutOfRangeError:
        pass
    else:
        raise AssertionError("Passing negative number to factorial did not raise an exception")"""


def test_factorial_negative():
    with pytest.raises(OutOfRangeError):
        factorial(-1)
