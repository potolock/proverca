

import pytest
from fixture.application import Application
# from fixture.application import Application_contact

@pytest.fixture(scope="session")
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture



# @pytest.fixture(scope="session")
# def app1(request):
    # fixture = Application_contact()
   #  request.addfinalizer(fixture.destroy)
    # return fixture


