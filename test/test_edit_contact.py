from model.contact import Contact

def test_test_add_contact(app):
    if app.contacts.count() == 0:
        app.contacts.add_contact(Contact(firstname = "NewContact"))
    app.contacts.edit_first_contact(Contact(firstname="New Test"))