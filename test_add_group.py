# -*- coding: utf-8 -*-

import pytest
from group import Group
from application import Application


@pytest.fixture
def app(request):
    fixture = Application
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_group(app):
    self.app.login( user="admin", password="secret")
    self.app.create_group( Group(name="jehfeorwijoe", header="ryg3ky4urgfk34utg", footer="3ye2qy3urk3quwyegf"))
    self.app.logout()

def test_add_empty_group(app):
    self.app.login( user="admin", password="secret")
    self.app.create_group( Group(name="", header="", footer=""))
    self.app.logout()


