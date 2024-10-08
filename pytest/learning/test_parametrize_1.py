import pytest

# simple square function
def square(num):
    return num * num

# with multiple input output parameter.
@pytest.mark.parametrize("num, ref", [(1,1), (2,4),(3,9),(4,16),(5,25)])
def test_square(num, ref):
    result = square(num)
    assert result == ref

