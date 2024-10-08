import pytest

# simple square
def square(num):
    return num * num

# multiple parameter skip function
@pytest.mark.parametrize("num",[1,2, pytest.param(3, marks=pytest.mark.skip) ,4,5])
def test_square(num):
    result = square(num)
    assert result == num ** 2