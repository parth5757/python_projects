import pytest

@pytest.fixture
def element_list(request):
    return list(range(request.param))