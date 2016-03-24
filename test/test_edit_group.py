from model.group import Group

def test_edit_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first_group((Group(name="edit test group", header="edit test group", footer="edit test group")))
    app.session.logout()