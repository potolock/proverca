# -*- coding: utf-8 -*-

from model.group import Contact
import pytest
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + ""*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])




testdata = [ Contact(firstname="", lastname="", company="", address="", email="", homepage="")] + [
            Contact(firstname=random_string("firstname", 10), lastname=random_string("lastname", 15),
                    company=random_string("company", 10), address=random_string("address", 20),
                      email=random_string("email", 10), homepage=random_string("homepage", 10))
    for i in range(5)
]


@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])

def test_add_contact(app, contact):
        old_contact_list = app.contact.get_contact_list()
        app.contact.fill_new(contact)
        assert len(old_contact_list) + 1 == app.contact.count()
        new_contact_list = app.contact.get_contact_list()
        old_contact_list.append(contact)
        assert sorted(old_contact_list, key=Contact.id_or_max) == sorted(new_contact_list, key=Contact.id_or_max)





