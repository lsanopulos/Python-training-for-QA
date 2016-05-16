from pytest_bdd import scenario
from .contact_steps import *

@scenario('contacts.feature', 'Add new contact')
def test_add_new_contact():
    pass

@scenario('groups.feature', 'Delete a group')
def test_delete_group():
    pass

@scenario('groups.feature', 'Modify a group')
def test_modify_group():
    pass