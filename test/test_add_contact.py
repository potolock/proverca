# -*- coding: utf-8 -*-

from model.group import Contact


def test_test_add_contact(app1):
    app1.session.login( username="admin", password="secret")
    app1.group.fill_new(Contact(firstname="natalia", lastname="krasnova", company="jhkjh", address="fewderf", email="email@email.ru", homepage="site.ru"))
    # app1.session.logout()

def test_add_empty_contact(app1):
     # app1.session.login( username="admin", password="secret")
     app1.group.fill_new(Contact(firstname="", lastname="", company="", address="", email="", homepage=""))
     app1.session.logout()

