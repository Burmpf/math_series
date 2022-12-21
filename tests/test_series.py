import pytest
from math_series.series import fibonacci, lucas, sum_series


def test_fib_1():
  actual = fibonacci(1)
  expected = 1
  assert actual == expected


def test_lucas_5():
  actual = lucas(5)
  expected = 11
  assert actual == expected

def test_sum_series_0():
  actual = sum_series(0)
  expected = 0
  assert actual == expected



def test_sum_series_321():
  actual = sum_series(3, 2, 1)
  expected = 4
  assert actual == expected