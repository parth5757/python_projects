import pytest
import sys

#simple square function 
def square(num):
    return num * num

# single test marked with skip which
@pytest.mark.skipif(
    sys.version_info > (3, 6), reason = "Test requires Python version <= 3.6!"
)
def test_square():
    num = 5
    result = square(num)
    assert result == num ** 2