# -*- coding: utf-8 -*-

from model.group import Contact


def test_test_add_contact(app):
    old_contact = app.contact.get_contact_list()
    app.contact.fill_new(Contact(firstname="natalia", lastname="krasnova", company="jhkjh", address="fewderf", email="email@email.ru", homepage="site.ru"))
    new_contact = app.contact.get_contact_list()
    assert len(old_contact) + 1 == len(new_contact)



def test_add_empty_contact(app):
    old_contact = app.contact.get_contact_list()
    app.contact.fill_new(Contact(firstname="", lastname="", company="", address="", email="", homepage=""))
    new_contact = app.contact.get_contact_list()
    assert len(old_contact) + 1 == len(new_contact)



