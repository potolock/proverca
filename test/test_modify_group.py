

from model.group import Group


def test_modify_group_name(app):
    app.session.login(username="admin", password="secret")
    app.group.modify_first_group(Group(name="Neww group"))


def test_modify_group_footer(app):
    app.session.login(username="admin", password="secret")
    app.group.modify_first_group_footer(Group(footer="Neww footer"))