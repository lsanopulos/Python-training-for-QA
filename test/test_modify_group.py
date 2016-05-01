from model.group import Group
import random

def test_modify_group_name(app, db):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name = "Created Group"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    #index = random.randrange(len(old_groups))
    #group = Group(name="New group")
    #group.id = old_groups[index].id
    #app.group.modify_group_by_index(index, group)
    mod_group = Group(name="New group", id=group.id)
    app.group.modify_group_by_id(group.id, mod_group)
    assert len(old_groups) == app.group.count()
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