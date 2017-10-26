

from model.group import Group
import random


def test_modify_group_name(app, db):
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    group.name = "Neww group"
    app.group.modify_group(group)
    assert len(old_groups) == app.group.count()
    new_groups = db.get_group_list()
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)



#def test_modify_group_footer(app):
#    old_groups = app.group.get_group_list()
#    app.group.modify_first_group(Group(footer="Neww footer"))
#    new_groups = app.group.get_group_list()
#    assert len(old_groups) == len(new_groups)