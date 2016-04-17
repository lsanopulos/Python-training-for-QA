from model.contact import Contact
from data.contacts import testdata
import pytest

#@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_test_add_contact(app, json_contacts):
    contact = json_contacts
    old_contacts = app.contacts.get_contacts_list()
    app.contacts.add_contact(contact)
    assert len(old_contacts) + 1 == app.contacts.count()
    new_contacts = app.contacts.get_contacts_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key = Contact.id_or_max) == sorted(new_contacts, key = Contact.id_or_max)






