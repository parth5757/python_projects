import pytest

@pytest.fixture
def initial_value():
    return 4  # or any other value you want to use in your test

def test_square(initial_value):
    assert initial_value ** 2 == 16  # Example assertion