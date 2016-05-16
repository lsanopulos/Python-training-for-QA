Scenario Outline: Add new contact
  Given a contact list
  Given a contact with <firstname>, <middlename>, <lastname>, <nickname>, <title>, <company>, <address>, <homePhone>, <mobilePhone>, <workPhone>, <fax>, <email>, <email2>, <email3>, <homepage>, <year>, <address2>, <phone2> and <notes>
  When I add the contact to the list
  Then the new gcontact list is equal to the old contact list with the edit contact

  Examples:
  | firstname   | middlename  | lastname   | nickname   | title   | company   | address   | homePhone  | mobilePhone  | workPhone  | fax  | email        | email2        | email3        | homepage   | year  | address2   | phone2  | notes   |
  | firstname1  | middlename1 | lastname1  | nickname1  | title1  | company1  | address1  | 123455678  | 90123456789  | 012345678  | 901  | email@ru.ru  | email2@ru.ru  | email3@ru.ru  | local      | 1976  | address21  | 234567  | notes1  |
  | firstname2  | middlename1 | lastname2  | nickname1  | title1  | company1  | address1  | 123455678  | 90123456789  | 012345678  | 901  | email@ru.ru  | email2@ru.ru  | email3@ru.ru  | local      | 1976  | address21  | 234567  | notes1  |