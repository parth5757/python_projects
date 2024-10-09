import pytest

# fixture that generates some inputs
# This take parameter this forwarded to the list
@pytest.fixture
def element_list(num_elements):
    return list(range(num_elements))