
# -*- coding: utf-8 -*-

from model.group import Contact

def test_test_modify_contact_firstname(app):
    if app.contact.count() ==0:
        app.contact.fill_new(Contact(lastname="tester"))
    old_contact = app.contact.get_contact_list()
    app.contact.modify_first_contact(Contact(firstname="Veronica"))
    new_contact = app.contact.get_contact_list()
    assert len(old_contact) == len(new_contact)


def test_test_modify_contact_address(app):
    if app.contact.count() ==0:
        app.contact.fill_new(Contact(company="tester"))
    old_contact = app.contact.get_contact_list()
    app.contact.modify_first_contact(Contact(address="Moscow"))
    new_contact = app.contact.get_contact_list()
    assert len(old_contact) == len(new_contact)
