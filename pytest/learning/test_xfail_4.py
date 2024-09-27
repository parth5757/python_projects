import pytest
import sys
# simple square function

def square(num):
    return num * num

# A single test marked with xfail with raise exception
@pytest.mark.xfail(raises=AssertionError)
def test_square():
    num = 5
    result = square(num)
    assert result == num ** 2
