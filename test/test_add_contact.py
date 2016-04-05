from model.contact import Contact

def test_test_add_contact(app):
    old_contacts = app.contacts.get_contacts_list()
    contact = Contact(firstname="Test", middlename="Tested", lastname="TestName", nickname="Tst", title="TestTitle", company="TestCompany", address="TestAddress", homePhone="123456", mobilePhone="78901234", workPhone="567890", fax="12345678", email="test@testcompany.com", homepage="testhomepage.com", year="1976", address2="test city", phone2="test town", notes="test notes")
    app.contacts.add_contact(contact)
    new_contacts = app.contacts.get_contacts_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key = Contact.id_or_max) == sorted(new_contacts, key = Contact.id_or_max)






