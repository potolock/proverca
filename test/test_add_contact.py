# -*- coding: utf-8 -*-

from model.group import Contact
import pytest
from data.add_contact import constant as testdata




@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])

def test_add_contact(app, contact):
        old_contact_list = app.contact.get_contact_list()
        app.contact.fill_new(contact)
        assert len(old_contact_list) + 1 == app.contact.count()
        new_contact_list = app.contact.get_contact_list()
        old_contact_list.append(contact)
        assert sorted(old_contact_list, key=Contact.id_or_max) == sorted(new_contact_list, key=Contact.id_or_max)





