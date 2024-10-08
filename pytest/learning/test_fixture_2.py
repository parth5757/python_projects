"""
Fixture function to generate an initial value for testing.
The initial value returned is 5.
"""
import pytest

# @pytest.fixture(scope="module")
@pytest.fixture(scope="function")
def initial_value():
    print("Generate initial value")
    return 5

# simple function that square a number
def square(num):
    return num * num

# cube function
def cube (num):
    return square(num) * num

# square function fixture test
def test_square(initial_value):
    result = square(initial_value)
    assert result == initial_value ** 2

# cube function fixture test
def test_cube(initial_value):
    result = cube(initial_value)
    assert result == initial_value ** 3

# 