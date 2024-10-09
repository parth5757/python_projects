import pytest

# (use in test_conftest_0.py)
# fixture that generates an input
# @pytest.fixture
# def initial_value():
#     return 5

# (use in test_conftest_1.py)
# simple fixtures that prints tests are starting
@pytest.fixture(autouse=True)
def log_start():
    print("Test is Starting")