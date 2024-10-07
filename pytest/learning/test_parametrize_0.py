import pytest

# square function
def square(num):
    return num * num

# parametrized test
@pytest.mark.parametrize("num", [1, 2, 3, 4, 5])
def test_square(num):
    result = square(num)
    assert result == num ** 2

