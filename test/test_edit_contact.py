from model.contact import Contact
import random
import pytest

def test_test_edit_contact(app, db):
    with pytest.allure.step('Checking, if contact list is empty'):
        if app.contacts.count() == 0:
            app.contacts.add_contact(Contact(firstname = "NewContact"))
    with pytest.allure.step('Given a contact list'):
        old_contacts = db.get_contacts_list()
    contact = random.choice(old_contacts)
    #index = randrange(len(old_contacts))
    with pytest.allure.step('Contact %s is modifying' % contact):
        con = Contact(firstname="New Test", id=contact.id)
        app.contacts.edit_contact_by_id(contact.id, con)
    #con = old_contacts[index]
    #index = int(contact.id)
    #app.contacts.edit_contact_by_index(index, con)
    assert len(old_contacts) == app.contacts.count()
    with pytest.allure.step('Then the new contact list is equal to the old list with the edited contact'):
        new_contacts = db.get_contacts_list()
        #old_contacts[index] = con
        old_contacts.remove(contact)
        old_contacts.append(con)
        assert sorted(old_contacts, key = Contact.id_or_max) == sorted(new_contacts, key = Contact.id_or_max)