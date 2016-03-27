from model.contact import Contact

def test_test_add_contact(app):
    app.contacts.edit_first_contact(Contact(firstname="New Test"))