# -*- coding: utf-8 -*-
import pytest
from fixture.application import Application

'''@pytest.fixture()
def app_con(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture'''


def test_test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.create_contact.add_contact()
    app.session.logout()


