import pytest

# fixture that generates input with yield keyword

@pytest.fixture

def initial_value():
    print("providing a value to test")
    yield 5
    print("Finished")