
# -*- coding: utf-8 -*-

from model.group import Contact

def test_test_modify_contact_firstname(app):
    if app.contact.count() ==0:
        app.contact.fill_new(Contact(lastname="tester"))
    app.contact.modify_first_contact(Contact(firstname="Veronica"))


def test_test_modify_contact_address(app):
    if app.contact.count() ==0:
        app.contact.fill_new(Contact(company="tester"))
    app.contact.modify_first_contact(Contact(address="Moscow"))
