import pytest

# simple square function
def square(num):
    return num * num

# with multiple input output parameter.
@pytest.mark.parametrize("num, ref", [(1,1), (2,4),(3,9),(4,16),(5,25)])
def test_square(num, ref):
    result = square(num)
    assert result == ref


# simple function that raise base to a power
def pow(base, exponent):
    return base ** exponent

# with multiple input output e parameter.
@pytest.mark.parametrize("base, exponent, ref", [(1,4,1), (2,5,32),(3,6,729)])
def test_pow(base, exponent, ref):
    result = pow(base, exponent)
    assert result == ref