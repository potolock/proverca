
# -*- coding: utf-8 -*-
from fixture.orm import ORMFixture
from model.group import Contact, Group
import random

db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")


def test_add_contact_in_group(app):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="NewGroup"))
    groups = db.get_group_list()
    group = random.choice(groups)
    old_contacts_in_group = db.get_contacts_in_group(group)
    if len(db.get_contact_list()) == 0 or len(db.get_contact_list()) == len(old_contacts_in_group):
        app.contact.fill_new(Contact(firstname="NEWSContact"))
    contacts = db.get_contacts_not_in_group(group)
    contact = random.choice(contacts)
    app.contact.add_contact_in_group(contact, group)
    new_contact_in_group = db.get_contacts_in_group(group)
    assert len(old_contacts_in_group) + 1 == len(new_contact_in_group)
    old_contacts_in_group.append(contact)
    assert sorted(old_contacts_in_group, key=Contact.id_or_max) == sorted(new_contact_in_group, key=Contact.id_or_max)





    # old_contacts = db.get_contact_list()
    # # if len(old_contacts) == 0:
    # #     app.group.fill_new(Contact(name="testerContact"))
    # contacts = random.choice(old_contacts)
    #
    # contact_not_gr = random.choice(db.get_contacts_not_in_group(group))
    # app.contact.add_contact_in_group(contacts)
    # assert len(old_contacts_in_group) + 1 == app.contact.count()
    # new_contact_in_group = db.get_contacts_in_group()
    # old_contacts_in_group.append(contacts)
    # assert sorted(old_contacts_in_group, key=Contact.id_or_max) == sorted(new_contact_in_group, key=Contact.id_or_max)





