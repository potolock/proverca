

import pytest
from fixture.application import Application_group

@pytest.fixture(scope="session")
def app(request):
    fixture = Application_group()
    request.addfinalizer(fixture.destroy)
    return fixture