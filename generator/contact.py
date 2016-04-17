from model.contact import Contact
import random
import string
import os.path
import jsonpickle
import getopt
import sys

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

def random_digits(prefix, maxlen):
    dig = string.digits
    return prefix + "".join([random.choice(dig) for i in range(random.randrange(maxlen))])

def random_mails(prefix, maxlen):
    mail_name = string.digits + string.ascii_letters + "_"*5
    domen_name = string.ascii_letters
    return prefix + "".join([random.choice(mail_name) for i in range(random.randrange(maxlen))]) + "@" + "".join([random.choice(domen_name) for i in range(random.randrange(maxlen))]) + "." + "".join([random.choice(domen_name) for i in range(random.randrange(3))])

def random_pages(prefix, maxlen):
    domen_name = string.ascii_letters
    return prefix + "".join([random.choice(domen_name) for i in range(random.randrange(maxlen))]) + "." + "".join([random.choice(domen_name) for i in range(random.randrange(3))])

testdata = [Contact(firstname="", middlename="", lastname="", nickname="", title="", company="", address="", homePhone="", mobilePhone="",
                    workPhone="", fax="", email="", email2="", email3="", homepage="", year="", address2="", phone2="", notes="")] + [
            Contact(firstname=random_string("firstname", 10), middlename=random_string("middlename", 10), lastname=random_string("lastname", 10),
                    nickname=random_string("nickname", 10), title=random_string("title", 10), company=random_string("company", 10),
                    address=random_string("address", 10), homePhone=random_digits("homephone", 12), mobilePhone=random_digits("mobilephone", 12),
                    workPhone=random_digits("workphone", 12), fax=random_digits("fax", 12), email=random_mails("email", 5),
                    email2=random_mails("email2", 5), email3=random_mails("email3", 5), homepage=random_pages("homepage", 8),
                    year=random_digits("year", 4), address2=random_string("address2", 10), phone2=random_digits("phone2", 12), notes=random_string("notes", 10))
            for i in range(n)
            ]
               #Group(name=name, header=header, footer=footer)
            #for name in ["", random_string("name", 10)]
            #for header in ["", random_string("header", 20)]
            #for footer in ["", random_string("footer", 20)]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)
with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent = 2)
    out.write(jsonpickle.encode(testdata))