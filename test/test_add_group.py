

from model.group import Group


def test_add_group(app):
    old_groups = app.group.get_group_list()
    print("!!!!!!!!!!! {}".format(sorted(old_groups, key=Group.id_or_max)))
    group = Group(name="jehfeorwijoe", header="ryg3ky4urgfk34utg", footer="3ye2qy3urk3quwyegf")
    app.group.create(group)
    new_groups = app.group.get_group_list()
    print("@@@@@@@@@@@@@@@@@@@@@ {}".format(sorted(new_groups, key=Group.id_or_max)))
    assert len (old_groups) + 1 == len (new_groups)
    old_groups.append(group)
    print("!!!!!!!!!!! {}".format(sorted(old_groups, key=Group.id_or_max)))
    assert sorted (old_groups, key=Group.id_or_max ) == sorted (new_groups, key=Group.id_or_max)

def test_add_empty_group(app):
     old_groups = app.group.get_group_list()
     group = Group(name="", header="", footer="")
     app.group.create(group)
     new_groups = app.group.get_group_list()
     assert len(old_groups) + 1 == len(new_groups)
     old_groups.append(group)
     assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


