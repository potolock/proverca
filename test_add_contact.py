# -*- coding: utf-8 -*-
import pytest
from group_contacty import Contact
from application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture



def test_test_add_contact(app):
    app.login( username="admin", password="secret")
    app.fill_new_contact( Contact(firstname="natalia", lastname="krasnova", company="jhkjh", address="fewderf", email="email@email.ru", homepage="site.ru"))
    app.submit()
    app.logout()

def test_test_add_empty_contact(app):
     app.login( username="admin", password="secret")
     app.fill_new_contact( Contact(firstname="", lastname="", company="", address="", email="", homepage=""))
     app.submit()
     app.logout()

