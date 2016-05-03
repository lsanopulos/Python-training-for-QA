from model.contact import Contact
from model.group import Group
from fixture.orm import ORMFixture
import random

def test_delete_contact_from_group(app, db):
    if app.contacts.count() == 0:
        app.contacts.add_contact(Contact(firstname = "NewContact"))
    base = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")
    old = base.get_contacts_in_group(Group(id="59"))
    contact = random.choice(old)
    app.contacts.delete_contact_from_group(contact.id)
    new = base.get_contacts_in_group(Group(id="59"))
    assert len(old) == len(new) + 1
