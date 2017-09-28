
from model.group import Contact


def test_delete_contact(app):
    if app.contact.count() == 0:
        app.contact.fill_new(Contact(firstname="tester"))
    app.contact.delete_first_contact()


