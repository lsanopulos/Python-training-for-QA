from model.contact import Contact
import random
import pytest

def test_delete_some_contact(app, db):
    with pytest.allure.step('Checking, if contact list is empty'):
        if app.contacts.get_contacts_list() == 0:
            app.contacts.add_contact(Contact(firstname = "NewContact"))
    with pytest.allure.step('Given a contact list'):
        old_contacts = db.get_contacts_list()
    contact = random.choice(old_contacts)
    #index = randrange(len(old_contacts))
    with pytest.allure.step('Contact %s is deleting' % contact):
        app.contacts.delete_contact_by_id(contact.id)
    assert len(old_contacts) - 1 == app.contacts.count()
    with pytest.allure.step('Then the new contact list is equal to the old list with the deleted contact'):
        new_contacts = db.get_contacts_list()
        #old_contacts[index:index+1] = []
        old_contacts.remove(contact)
        assert old_contacts == new_contacts