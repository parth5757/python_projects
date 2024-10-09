import pytest

# simple square function

def square(num):
    return num * num

# A single test marked with xfail with reason
@pytest.mark.xfail(reason="Any reason for this")
def test_square():
    num = 5
    result = square(num)
    assert result == num **2
