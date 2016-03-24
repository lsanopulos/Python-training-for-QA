def test_test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contacts.edit_first_contact()
    app.session.logout()