from pytest_bdd import given, when, then
from model.contact import Contact
import random

@given('a contact list')
def contact_list(db):
    return db.get_contacts_list()

@given('a contact with <lastname>, <firstname>')
def new_contact(firstname, middlename, lastname, nickname, title, company, address, homePhone, mobilePhone, workPhone, fax, email, email2, email3, homepage, year, address2, phone2, notes):
    return Contact(firstname = firstname, middlename = middlename, lastname = lastname, nickname = nickname, title = title, company = company, address = address, homePhone = homePhone, mobilePhone = mobilePhone, workPhone = workPhone, fax = fax, email = email, email2 = email2, email3 = email3, homepage = homepage, year = year, address2 = address2, phone2 = phone2, notes = notes)

@when('I add the contact to the list')
def add_new_contact(app, new_contact):
    app.contacts.add_contact(Contact(new_contact))

@then('the new gcontact list is equal to the old contact list with the new contact')
def verify_contact_add(db, contact_list, new_contact):
    old_contacts = contact_list
    new_contacts = db.get_contacts_list()
    old_contacts.append(new_contact)
    assert sorted(old_contacts, key = Contact.id_or_max) == sorted(new_contacts, key = Contact.id_or_max)

@given('a non-empty group list')
def non_empty_group_list(app, db):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name='SomeName'))
    return db.get_group_list()

@given('a random group from the list')
def random_group(non_empty_group_list):
    return random.choice(non_empty_group_list)

@when('I delete the group from the list')
def delete_group(app, random_group):
    app.group.delete_group_by_id(random_group.id)

@then('the new group list is equal to the old group list without the deleted group')
def verify_group_deleted(db, non_empty_group_list, random_group, app, check_ui):
    old_groups = non_empty_group_list
    new_groups = db.get_group_list()
    old_groups.remove(random_group)
    assert old_groups == new_groups
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)

@when('I modify the group from the list')
def modify_group(app, random_group):
    mod_group = Group(name="Modified group", id=random_group.id)
    app.group.modify_group_by_id(random_group.id, mod_group)

@then('the new group list is equal to the old group list')
def verify_group_modified(db, non_empty_group_list, random_group):
    old_groups = non_empty_group_list
    new_groups = db.get_group_list()
    #old_groups.remove(random_group)
    #old_groups.append(modify_group)
    #assert sorted(old_groups, key = Group.id_or_max) == sorted(new_groups, key = Group.id_or_max)
    assert len(old_groups) == len(new_groups)
