from model.contact import Contact

def test_test_add_contact(app):
    app.contacts.add_contact(Contact(firstname="Test", middlename="Tested", lastname="TestName", nickname="Tst", title="TestTitle", company="TestCompany", address="TestAddress", homePhone="123456", mobilePhone="78901234", workPhone="567890", fax="12345678", email="test@testcompany.com", homepage="testhomepage.com", year="1976", address2="test city", phone2="test town", notes="test notes"))