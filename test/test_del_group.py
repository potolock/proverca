
from model.group import Group



def test_test_delete_first_group(app):
    app.group.delete_first_group()
    if app.group.cont() == 0:
        app.group.create (Group(name="test"))
    app.group.delete_first_group()
