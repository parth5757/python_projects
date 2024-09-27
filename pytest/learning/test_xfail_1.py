import pytest

# simple square function

def square(num):
    return num * num

# A single test marked with xfail
def test_square():
    pytest.xfail()
    num = 5
    result = square(num)
    assert result == num **2
    