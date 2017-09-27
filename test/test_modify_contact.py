
# -*- coding: utf-8 -*-

from model.group import Contact

def test_test_modify_contact_firstname(app):
    app.contact.modify_first_contact(Contact(firstname="Veronica"))


def test_test_modify_contact_address(app):
    app.contact.modify_first_contact(Contact(address="Moscow"))
