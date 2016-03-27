# -*- coding: utf-8 -*-
from model.group import Group

def test_test_add_group(app):
    app.group.create(Group(name="test group", header="test group", footer="test group"))

def test_test_add_emp_group(app):
    app.group.create(Group(name="", header="", footer=""))

