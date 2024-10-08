import pytest
import math

# simple function that raise base to a power
def pow(base, exponent):
    return base ** exponent

# with multiple input output parameter.
@pytest.mark.parametrize("base", [1,2,3])
@pytest.mark.parametrize("exponent", [4,5,6])
def test_pow(base, exponent):
    # test if our function matches math.pow
    result = pow(base, exponent)
    print(result)
    assert result == math.pow(base, exponent)


print(pow(2 ,5))