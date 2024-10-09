import pytest
import sys
# simple square function

def square(num):
    return num * num

# A single test marked with xfail with reason
@pytest.mark.xfail(sys.version_info > (3,6), reason="Any reason for this")
def test_square():
    num = 5
    result = square(num)
    assert result == num **2
