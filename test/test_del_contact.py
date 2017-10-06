
from model.group import Contact
from random import randrange


def test_delete_some_contact(app):
    if app.contact.count() == 0:
        app.contact.fill_new(Contact(firstname="tester"))
    old_contact_list = app.contact.get_contact_list()
    index = randrange(len(old_contact_list))
    app.contact.delete_contact_by_index (index)
    assert len(old_contact_list) - 1 == app.contact.count()
    new_contact_list = app.contact.get_contact_list()
    old_contact_list[index:index +1] = []
    assert old_contact_list == new_contact_list


# def test_delete_contact(app):
#     if app.contact.count() == 0:
#         app.contact.fill_new(Contact(firstname="tester"))
#     old_contact_list = app.contact.get_contact_list()
#     app.contact.delete_first_contact()
#     assert len(old_contact_list) - 1 == app.contact.count()
#     new_contact_list = app.contact.get_contact_list()
#     old_contact_list[0:1] = []
#     assert old_contact_list == new_contact_list

