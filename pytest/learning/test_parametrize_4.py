import pytest

# simple square function
def square(num):
    return num * num

# 
@pytest.mark.parametrize(
    "num",
    [
        pytest.param(-1, id="negative"),
        pytest.param(0, id="zero"),
        pytest.param(1, id="positive")
    ],
)
def test_square(num):
    result = square(num)
    assert result == num ** 2
        