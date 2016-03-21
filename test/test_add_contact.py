# -*- coding: utf-8 -*-
import pytest
from fixture.application_contact import Application_contact

@pytest.fixture()
def app_con(request):
    fixture = Application_contact()
    request.addfinalizer(fixture.destroy_contact)
    return fixture


def test_test_add_contact(app_con):
    app_con.session_contact.login()
    app_con.create_contact.add_contact()
    app_con.session_contact.logout()


