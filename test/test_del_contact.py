from model.contact import Contact

def test_delete_first_contact(app):
    if app.contacts.count() == 0:
        app.contacts.add_contact(Contact(firstname = "NewContact"))
    old_contacts = app.contacts.get_contacts_list()
    app.contacts.delete_first_contact()
    new_contacts = app.contacts.get_contacts_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts[0:1] = []
    assert old_contacts == new_contacts