# A simple pytest skipping example without decorated
import pytest

# simple square function

def square(num):
    return num * num

# test with the reason we want to return why we add this test or add any notes
@pytest.mark.skip(reason="Look! We are skipping this test")
def test_square():
    num = 5
    result = square(num)
    assert result == num **2