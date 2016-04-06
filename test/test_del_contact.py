from model.contact import Contact
from random import randrange
def test_delete_first_contact(app):
    if app.contacts.count() == 0:
        app.contacts.add_contact(Contact(firstname = "NewContact"))
    old_contacts = app.contacts.get_contacts_list()
    index = randrange(len(old_contacts))
    app.contacts.delete_contact_by_index(index)
    assert len(old_contacts) - 1 == app.contacts.count()
    new_contacts = app.contacts.get_contacts_list()
    old_contacts[index:index+1] = []
    assert old_contacts == new_contacts