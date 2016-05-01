from model.contact import Contact
import random

def test_delete_some_contact(app, db):
    if app.contacts.get_contacts_list() == 0:
        app.contacts.add_contact(Contact(firstname = "NewContact"))
    old_contacts = db.get_contacts_list()
    contact = random.choice(old_contacts)
    #index = randrange(len(old_contacts))
    app.contacts.delete_contact_by_id(contact.id)
    assert len(old_contacts) - 1 == app.contacts.count()
    new_contacts = db.get_contacts_list()
    #old_contacts[index:index+1] = []
    old_contacts.remove(contact)
    assert old_contacts == new_contacts