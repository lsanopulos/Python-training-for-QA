from model.contact import Contact

def test_delete_first_contact(app):
    if app.contacts.count() == 0:
        app.contacts.add_contact(Contact(firstname = "NewContact"))
    app.contacts.delete_first_contact()