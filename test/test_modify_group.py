

from model.group import Group


def test_modify_group_name(app):
    if app.group.count() == 0:
       app.group.create (Group(name="tester"))
    app.group.modify_first_group(Group(name="Neww group"))



def test_modify_group_footer(app):
    if app.group.count() == 0:
       app.group.create (Group(footer="tester"))
    app.group.modify_first_group(Group(footer="Neww footer"))