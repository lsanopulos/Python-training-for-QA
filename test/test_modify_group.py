from model.group import Group
import random
import pytest

def test_modify_group_name(app, db):
    with pytest.allure.step('Checking, if group list is empty'):
        if len(db.get_group_list()) == 0:
            app.group.create(Group(name = "Created Group"))
    with pytest.allure.step('Given a group list'):
        old_groups = db.get_group_list()
    group = random.choice(old_groups)
    #index = random.randrange(len(old_groups))
    #group = Group(name="New group")
    #group.id = old_groups[index].id
    #app.group.modify_group_by_index(index, group)
    with pytest.allure.step('Group %s is editing' % group):
        mod_group = Group(name="New group", id=group.id)
        app.group.modify_group_by_id(group.id, mod_group)
    assert len(old_groups) == app.group.count()
    with pytest.allure.step('Then the new group list is equal to the old list with the edited group'):
        new_groups = db.get_group_list()
        #old_groups[index] = group
        old_groups.remove(group)
        old_groups.append(mod_group)
        assert sorted(old_groups, key = Group.id_or_max) == sorted(new_groups, key = Group.id_or_max)


'''def test_modify_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(header = "Created Header"))
    old_groups = app.group.get_group_list()
    app.group.modify_first_group(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)'''