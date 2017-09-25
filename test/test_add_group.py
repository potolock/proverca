

from model.group import Group


def test_add_group(app):
     app.session.login(username="admin", password="secret")
     app.group.create(Group(name="jehfeorwijoe", header="ryg3ky4urgfk34utg", footer="3ye2qy3urk3quwyegf"))
     # app.session.logout()

def test_add_empty_group(app):
    # app.session.login(user="admin", password="secret")
    app.group.create(Group(name="", header="", footer=""))
    app.session.logout()



