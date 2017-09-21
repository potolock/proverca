# -*- coding: utf-8 -*-
import pytest

from fixture.application import Application_contact
from model.group import Group


@pytest.fixture
def app(request):
    fixture = Application_contact()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_test_add_group(app):
    app.session.login(username="admin", password="secret")
    app.create(Group(name="jehfeorwijoe", header="ryg3ky4urgfk34utg", footer="3ye2qy3urk3quwyegf"))
    app.session.logout()

def test_test_add_empty_group(app):
    app.session.login(username="admin", password="secret")
    app.create(Group(name="", header="", footer=""))
    app.session.logout()

