
from model.group import Contact
from timeit import timeit




def test_contact_list(app, db):
    ui_list = app.contact.get_contact_list()
    def clean(contact):
        return Contact(id=contact.id, firstname=contact.firstname, lastname=contact.lastname, company=contact.company,
                       homepage=contact.homepage, address=contact.address.strip())
    db_list = map(clean, db.get_contact_list())
    assert sorted(ui_list, key=Contact.id_or_max) == sorted(db_list, key=Contact.id_or_max)
