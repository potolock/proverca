# -*- coding: utf-8 -*-

from model.group import Contact


def test_add_contact(app):
    old_contact_list = app.contact.get_contact_list()
    contact = Contact(firstname="natalia", lastname="krasnova", company="jhkjh", address="fewderf",
                      email="", homepage="site.ru")
    app.contact.fill_new(contact)
    new_contact_list = app.contact.get_contact_list()
    assert len(old_contact_list) + 1 == len(new_contact_list)
    old_contact_list.append(contact)
    assert  sorted (old_contact_list, key=Contact.id_or_max) == sorted (new_contact_list, key=Contact.id_or_max)


def test_add_empty_contact(app):
   old_contact_list = app.contact.get_contact_list()
   contact = Contact(firstname="", lastname="", company="", address="", email="", homepage="")
   app.contact.fill_new(contact)
   new_contact_list = app.contact.get_contact_list()
   assert len(old_contact_list) + 1 == len(new_contact_list)
   old_contact_list.append(contact)
   assert sorted(old_contact_list, key=Contact.id_or_max) == sorted(new_contact_list, key=Contact.id_or_max)


