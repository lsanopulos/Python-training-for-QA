from model.contact import Contact
import random

def test_test_edit_contact(app, db):
    if app.contacts.count() == 0:
        app.contacts.add_contact(Contact(firstname = "NewContact"))
    old_contacts = db.get_contacts_list()
    contact = random.choice(old_contacts)
    #index = randrange(len(old_contacts))
    con = Contact(firstname="New Test", id=contact.id)
    #con = old_contacts[index]
    #index = int(contact.id)
    #app.contacts.edit_contact_by_index(index, con)
    app.contacts.edit_contact_by_id(contact.id, con)
    assert len(old_contacts) == app.contacts.count()
    new_contacts = db.get_contacts_list()
    #old_contacts[index] = con
    old_contacts.remove(contact)
    old_contacts.append(con)
    assert sorted(old_contacts, key = Contact.id_or_max) == sorted(new_contacts, key = Contact.id_or_max)