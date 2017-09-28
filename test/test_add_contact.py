# -*- coding: utf-8 -*-

from model.group import Contact


def test_test_add_contact(app):
    app.contact.fill_new(Contact(firstname="natalia", lastname="krasnova", company="jhkjh", address="fewderf", email="email@email.ru", homepage="site.ru"))
    # app.contact.submit()


#def test_add_empty_contact(app):
     #app.contact.fill_new(Contact(firstname="", lastname="", company="", address="", email="", homepage=""))
     #app.contact.submit()


