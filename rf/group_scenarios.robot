*** Settings ***
Library  rf.AddressBook
Library  Collections
Suite Setup  Init Fixtures
Suite Teardown  Destroy Fixtures

*** Test Cases ***
Add new group
    ${old_list}=  Get Group List
    ${group}=  New Group  name1  header1  footer1
    Create Group  ${group}
    ${new_list}=  Get Group List
    append to list  ${old_list}  ${group}
    Group Lists Should Be Equal  ${new_list}  ${old_list}

Delete group
    ${old_list}=  Get Group List
    ${length}=  get length  ${old_list}
    ${index}=  evaluate  random.randrange (len(${length}))  random
    ${group}=  get from list  ${old_list}  ${index}
    Delete Group  ${group}
    ${new_list}=  Get Group List
    remove values from list  ${old_list}  ${group}
    Group Lists Should Be Equal  ${new_list}  ${old_list}