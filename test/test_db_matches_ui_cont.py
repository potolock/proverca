
from model.group import Contact
from timeit import timeit




def test_contact_list(app, db):
    ui_list = app.contact.get_contact_list()
    db_list = db.get_contact_list()
    assert sorted(ui_list, key=Contact.id_or_max) == sorted(db_list, key=Contact.id_or_max)
