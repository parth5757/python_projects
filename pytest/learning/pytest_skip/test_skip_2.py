# A simple pytest skipping example without decorated
import pytest

# simple square function

def square(num):
    return num * num

# A single test marked with test
def test_square():
    pytest.skip()
    num = 5
    result = square(num)
    assert result == num **2
    