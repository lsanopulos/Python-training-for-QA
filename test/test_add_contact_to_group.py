from model.contact import Contact
from model.group import Group
from fixture.orm import ORMFixture
import random

def test_add_contact_to_group(app, db):
    base = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")
    if app.contacts.count() == 0:
        app.contacts.add_contact(Contact(firstname = "NewContact"))
    old_contacts = db.get_contacts_list()
    old = base.get_contacts_in_group(Group(id="59"))
    contact = random.choice(old_contacts)
    #old_groups = db.get_group_list()
    app.contacts.add_contact_to_group(contact.id)
    new = base.get_contacts_in_group(Group(id="59"))
    assert len(old) == len(new) - 1



