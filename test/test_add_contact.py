# -*- coding: utf-8 -*-
import pytest

from fixture.application import Application_contact
from model.group import Contact


@pytest.fixture
def app(request):
    fixture = Application_contact()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_test_add_contact(app):
    app.session.login( username="admin", password="secret")
    app.group.fill_new(Contact(firstname="natalia", lastname="krasnova", company="jhkjh", address="fewderf", email="email@email.ru", homepage="site.ru"))
    app.session.logout()

def test_test_add_empty_contact(app):
     app.session.login( username="admin", password="secret")
     app.group.fill_new(Contact(firstname="", lastname="", company="", address="", email="", homepage=""))
     app.session.logout()

