import pytest

# Simple function for making elements sum

def sum_elements(elements):
    total = 0
    for i in elements:
        total += i
    return total

# test function which indirect parameter use from conftest declare in pytest mark

@pytest.mark.parametrize("element_list)", [1,2,3,4,5], indirect=True)
def test_sum(element_list):
    result = sum_elements(element_list)
    assert result == sum(element_list)