import pytest

@pytest.fixture(scope="session")
def testdatacredentials(request):
    return request.param
