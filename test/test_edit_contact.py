from model.contact import Contact

def test_test_add_contact(app):
    if app.contacts.count() == 0:
        app.contacts.add_contact(Contact(firstname = "NewContact"))
    old_contacts = app.contacts.get_contacts_list()
    con = Contact(firstname="New Test")
    con.id = old_contacts[0].id
    app.contacts.edit_first_contact(con)
    assert len(old_contacts) == app.contacts.count()
    new_contacts = app.contacts.get_contacts_list()
    old_contacts[0] = con
    assert sorted(old_contacts, key = Contact.id_or_max) == sorted(new_contacts, key = Contact.id_or_max)