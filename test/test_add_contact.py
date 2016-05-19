from model.contact import Contact
from data.contacts import testdata
import pytest
import random

#@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_test_add_contact(app, db, json_contacts):
    with pytest.allure.step('Given a contact list'):
        old_contacts = db.get_contacts_list()
    contact = json_contacts
    with pytest.allure.step('When I add contact %s to the list' % contact):
        app.contacts.add_contact(contact)
    #assert len(old_contacts) + 1 == app.contacts.count()
    with pytest.allure.step('Then the new contact list is equal to the old list with the edit contact'):
        new_contacts = db.get_contacts_list()
        old_contacts.append(contact)
        assert sorted(old_contacts, key = Contact.id_or_max) == sorted(new_contacts, key = Contact.id_or_max)


