# -*- coding: utf-8 -*-

from model.group import Contact

def test_add_contact(app, db, json_contact):
        contact = json_contact
        old_contact_list = db.get_contact_list()
        app.contact.fill_new(contact)
        assert len(old_contact_list) + 1 == app.contact.count()
        new_contact_list = db.get_contact_list()
        old_contact_list.append(contact)
        assert sorted(old_contact_list, key=Contact.id_or_max) == sorted(new_contact_list, key=Contact.id_or_max)





