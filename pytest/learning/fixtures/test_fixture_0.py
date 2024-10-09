import pytest

# A fixture that genrates value
@pytest.fixture
def initial_value():
    return 5

#squares function
def square(num):
    return num * num

# test function for square function and parameter value initial comming from the fixture function
def test_square(initial_value):
    result = square(initial_value)
    assert result == initial_value ** 2