

from model.group import Group


def test_add_group(app):
    old_groups = app.group.get_group_list()
    app.group.create(Group(name="jehfeorwijoe", header="ryg3ky4urgfk34utg", footer="3ye2qy3urk3quwyegf"))
    new_groups = app.group.get_group_list()
    assert len (old_groups) + 1 == len (new_groups)

def test_add_empty_group(app):
     old_groups = app.group.get_group_list()
     group = Group(name="", header="", footer="")
     app.group.create(group)
     new_groups = app.group.get_group_list()
     assert len(old_groups) + 1 == len(new_groups)



