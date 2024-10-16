import pytest

# adds a argparse-like option

def pytest_addoption(parser):
    parser.addoption("--name", action="store", default="Parth", help="Choose a name!")

# A simple fixture that gets our name option

@pytest.fixture
def name(request):
    return request.config.getoption("--name")

