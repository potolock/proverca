
# -*- coding: utf-8 -*-

from model.group import Contact
import random



def test_modify_contact(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.fill_new(Contact(firstname="tester"))
    old_contact_list = db.get_contact_list()
    contact = random.choice(old_contact_list)
    contact.firstname = "veronica"
    app.contact.modify_contact(contact)
    assert len(old_contact_list) ==  app.contact.count()
    new_contact_list = db.get_contact_list()
    assert sorted(old_contact_list, key=Contact.id_or_max) == sorted(new_contact_list, key=Contact.id_or_max)


#def test_test_modify_contact_address(app):
#    if app.contact.count() ==0:
#        app.contact.fill_new(Contact(company="tester"))
#   old_contact = app.contact.get_contact_list()
#    app.contact.modify_first_contact(Contact(address="Moscow"))
#    new_contact = app.contact.get_contact_list()
 #   assert len(old_contact) == len(new_contact)
