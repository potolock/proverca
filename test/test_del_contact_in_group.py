from time import sleep

from fixture.orm import ORMFixture
from model.group import Contact, Group
import random

db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")


def test_delete_contact_in_group(app):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="NewGroup2"))
    groups = db.get_group_list()
    group = random.choice(groups)
    if len(db.get_contacts_in_group(group)) == 0:
        app.contact.add_contact_in_group(Contact(firstname="udalenie"))
    old_contacts_in_group = db.get_contacts_in_group(group)
    contact = random.choice(old_contacts_in_group)
    app.contact.delete_contact_in_group(contact, group)
    new_contact_in_group = db.get_contacts_in_group(group)
    assert len(old_contacts_in_group) - 1 == len(new_contact_in_group)
    old_contacts_in_group.remove(contact)
    assert sorted(old_contacts_in_group, key=Contact.id_or_max) == sorted(new_contact_in_group, key=Contact.id_or_max)



# def test_delete_contact_in_group(app, db, check_ui):
#     if len(db.get_contact_list()) == 0:
#         app.contact.fill_new(Contact(firstname="udalenie"))
#     old_contact_list = db.get_contact_list()
#     contact = random.choice(old_contact_list)
#     app.contact.delete_contact_by_id(contact.id)
#     new_contact_list = db.get_contact_list()
#     old_contact_list.remove(contact)
#     assert old_contact_list == new_contact_list
#     if check_ui:
#         assert sorted(new_contact_list, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
#                                                                          key=Contact.id_or_max)