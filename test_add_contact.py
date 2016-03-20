# -*- coding: utf-8 -*-

import pytest
from application_contact import Application_contact

@pytest.fixture()
def app_con(request):
    fixture = Application_contact()
    request.addfinalizer(fixture.destroy_contact)
    return fixture


def test_test_add_contact(app_con):
    app_con.login()
    app_con.add_contact()
    app_con.logout()


