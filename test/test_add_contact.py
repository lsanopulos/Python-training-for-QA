
def test_test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.create_contact.add_contact()
    app.session.logout()


