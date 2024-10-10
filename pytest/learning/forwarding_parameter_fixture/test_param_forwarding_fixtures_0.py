import pytest

# calculate sum of list element
def sum_elements(elements):
    total = 0
    for i in elements:
        total += i
    return total

# 
@pytest.mark.parametrize("num_elements", [1,2,3,4,5])
def test_sum(element_list, num_elements):
    result = sum_elements(element_list)
    assert result == sum_elements(element_list)