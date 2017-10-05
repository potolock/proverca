
# -*- coding: utf-8 -*-

from model.group import Contact

def test_modify_contact_firstname(app):
    if app.contact.count() == 0:
        app.contact.fill_new(Contact(lastname="tester"))
    old_contact_list = app.contact.get_contact_list()
    contact = Contact(firstname="tretret")
    contact.id = old_contact_list[0].id
    app.contact.modify_first_contact(contact)
    assert len(old_contact_list) ==  app.contact.count()
    new_contact = app.contact.get_contact_list()
    old_contact_list[0] = contact
    assert sorted(old_contact_list, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)


#def test_test_modify_contact_address(app):
#    if app.contact.count() ==0:
#        app.contact.fill_new(Contact(company="tester"))
#   old_contact = app.contact.get_contact_list()
#    app.contact.modify_first_contact(Contact(address="Moscow"))
#    new_contact = app.contact.get_contact_list()
 #   assert len(old_contact) == len(new_contact)
