import pytest

# simple square function

def square(num):
    return num * num

# A single test marked with test
@pytest.mark.skip()
def test_square():
    num = 5
    result = square(num)
    assert result == num **2
    