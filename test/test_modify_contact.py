
# -*- coding: utf-8 -*-

from model.group import Contact
from random import randrange



def test_modify_contact_by_index(app):
    if app.contact.count() == 0:
        app.contact.fill_new(Contact(lastname="ivanova"))
    old_contact_list = app.contact.get_contact_list()
    index = randrange(len(old_contact_list))
    contact = Contact(firstname="veronica")
    contact.id = old_contact_list[index].id
    app.contact.modify_contact_by_index(index, contact)
    assert len(old_contact_list) ==  app.contact.count()
    new_contact_list = app.contact.get_contact_list()
    old_contact_list[index] = contact
    assert sorted(old_contact_list, key=Contact.id_or_max) == sorted(new_contact_list, key=Contact.id_or_max)


#def test_test_modify_contact_address(app):
#    if app.contact.count() ==0:
#        app.contact.fill_new(Contact(company="tester"))
#   old_contact = app.contact.get_contact_list()
#    app.contact.modify_first_contact(Contact(address="Moscow"))
#    new_contact = app.contact.get_contact_list()
 #   assert len(old_contact) == len(new_contact)
