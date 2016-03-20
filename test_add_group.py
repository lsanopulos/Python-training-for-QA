# -*- coding: utf-8 -*-
import pytest
from group import Group
from application import Application

@pytest.fixture()
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_test_add_group(app):
    success = True
    app.login(username="admin", password="secret")
    app.create_group(Group(name="test group", header="test group", footer="test group"))
    app.logout()

def test_test_add_emp_group(app):
    success = True
    app.login(username="admin", password="secret")
    app.create_group(Group(name="", header="", footer=""))
    app.logout()

