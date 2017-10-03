# -*- coding: utf-8 -*-

from model.group import Contact


def test_test_add_contact(app):
    old_contact = app.contact.get_contact_list()
    contact = Contact(firstname="natalia", lastname="krasnova", company="jhkjh", address="fewderf", email="email@email.ru", homepage="site.ru")
    app.contact.fill_new(contact)
    new_contact = app.contact.get_contact_list()
    assert len(old_contact) + 1 == len(new_contact)
    old_contact.append (contact)
    assert  sorted (old_contact, key=Contact.id_or_max) == sorted (new_contact, key=Contact.id_or_max)


def test_add_empty_contact(app):
    old_contact = app.contact.get_contact_list()
    contact = Contact(firstname="natalia", lastname="krasnova", company="jhkjh", address="fewderf", email="email@email.ru", homepage="site.ru")
    app.contact.fill_new(contact)
    new_contact = app.contact.get_contact_list()
    assert len(old_contact) + 1 == len(new_contact)
    old_contact.append(contact)
    assert sorted(old_contact, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)


