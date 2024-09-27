import pytest
import sys
# simple square function

def square(num):
    return num * num

# A single test marked with xfail for true or false condition(Note: By default it will be )
@pytest.mark.xfail(strict=True)
def test_square():
    num = 5
    result = square(num)
    assert result == num ** 20
