# -*- coding: utf-8 -*-
from model.group import Group
from data.groups import testdata
import pytest

#@pytest.mark.parametrize("group", testdata, ids=[repr(x) for x in testdata])
def test_test_add_group(app, db, json_groups):
    with pytest.allure.step('Given a group list'):
        old_groups = db.get_group_list()
    group = json_groups
    with pytest.allure.step('When I add group %s to the list' % group):
        app.group.create(group)
    #assert len(old_groups) + 1 == app.group.count()
    with pytest.allure.step('Then the new group list is equal to the old list with the edit group'):
        new_groups = db.get_group_list()
        old_groups.append(group)
        assert sorted(old_groups, key = Group.id_or_max) == sorted(new_groups, key = Group.id_or_max)