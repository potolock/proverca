


def test_delete_contact(app1):
    app1.session.login(username="admin", password="secret")
    app1.group.delete_first_contact()
    app1.session.logout()