import pytest
my_import = pytest.importorskip("mymodule")

# simple square function

def square(num):
    return num * num

# A single test marked with test
def test_square():
    num = 5
    result = square(num)
    assert result == num **2