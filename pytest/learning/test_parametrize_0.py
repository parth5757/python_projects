import pytest

# square function
def square(num):
    return num * num

# parametrized test
# @pytest.mark.skip()
@pytest.mark.parametrize("num", [1, 2, 3, 4, 5])
def test_square(num):
    result = square(num)
    assert result == num ** 2

# multiple parameter at same time
@pytest.mark.parametrize("test_input,expected", [("3+5", 8), ("2+4", 6), ("6*9", 54)])
def test_eval(test_input, expected):
    assert eval(test_input) == expected