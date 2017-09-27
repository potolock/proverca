
# -*- coding: utf-8 -*-

from model.group import Contact

def test_test_modify_contact_firstname(app):
    # app.session.login( username="admin", password="secret")
    app.contact.modify_first_contact(Contact(firstname="Veronica"))
    # app.contact.submit()

def test_test_modify_contact_address(app):
    # app.session.login(username="admin", password="secret")


    app.contact.modify_first_contact(Contact(address="Moscow"))
    # app.contact.submit()