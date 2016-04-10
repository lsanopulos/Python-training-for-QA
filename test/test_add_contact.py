from model.contact import Contact

def test_test_add_contact(app):
    old_contacts = app.contacts.get_contacts_list()
    contact = Contact(firstname="Test", middlename="Tested", lastname="TestName", nickname="Tst", title="TestTitle", company="TestCompany", address="TestAddress", homePhone="123456", mobilePhone="78901234", workPhone="567890", fax="12345678", email="test@testcompany.com", email2="test2@testcompany.com", email3="test3@testcompany.com", homepage="testhomepage.com", year="1976", address2="test city", phone2="98765432", notes="test notes")
    app.contacts.add_contact(contact)
    assert len(old_contacts) + 1 == app.contacts.count()
    new_contacts = app.contacts.get_contacts_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key = Contact.id_or_max) == sorted(new_contacts, key = Contact.id_or_max)






