from model.contact import Contact
from random import randrange

def test_test_add_contact(app):
    if app.contacts.count() == 0:
        app.contacts.add_contact(Contact(firstname = "NewContact"))
    old_contacts = app.contacts.get_contacts_list()
    index = randrange(len(old_contacts))
    con = Contact(firstname="New Test")
    con.id = old_contacts[index].id
    app.contacts.edit_contact_by_index(index, con)
    assert len(old_contacts) == app.contacts.count()
    new_contacts = app.contacts.get_contacts_list()
    old_contacts[index] = con
    assert sorted(old_contacts, key = Contact.id_or_max) == sorted(new_contacts, key = Contact.id_or_max)