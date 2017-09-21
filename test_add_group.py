
import pytest

from application_group import Application
from model.group import Group


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_test_add_group(app):
     app.login(user="admin", password="secret")
     app.create_group( Group(name="jehfeorwijoe", header="ryg3ky4urgfk34utg", footer="3ye2qy3urk3quwyegf"))
     app.logout()

def test_test_add_empty_group(app):
    app.login(user="admin", password="secret")
    app.create_group( Group(name="", header="", footer=""))
    app.logout()



