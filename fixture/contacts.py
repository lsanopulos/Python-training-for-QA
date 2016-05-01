from model.contact import Contact
import re


class CreateContactHelper:
    def __init__(self, app):
        self.app = app

    def fill_contact_form(self, contact):
        wd = self.app.wd
        # fill contact form
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("middlename", contact.middlename)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("nickname", contact.nickname)
        self.change_field_value("title", contact.title)
        self.change_field_value("company", contact.company)
        self.change_field_value("address", contact.address)
        self.change_field_value("home", contact.homePhone)
        self.change_field_value("mobile", contact.mobilePhone)
        self.change_field_value("work", contact.workPhone)
        self.change_field_value("fax", contact.fax)
        self.change_field_value("email", contact.email)
        self.change_field_value("email2", contact.email2)
        self.change_field_value("email3", contact.email3)
        self.change_field_value("homepage", contact.homepage)
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[5]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[5]").click()
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[4]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[4]").click()
        self.change_field_value("byear", contact.year)
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[3]//option[6]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[3]//option[6]").click()
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[4]//option[4]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[4]//option[4]").click()
        self.change_field_value("address2", contact.address2)
        self.change_field_value("phone2", contact.phone2)
        self.change_field_value("notes", contact.notes)

    def submit_contact_creation(self):
        wd = self.app.wd
        # submit contact creation
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def return_to_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()

    def add_contact(self, contact):
        wd = self.app.wd
        # add contact
        if not (wd.current_url.endswith("/edit.php") and len(wd.find_elements_by_name("submit")) > 0):
            wd.find_element_by_link_text("add new").click()
        self.fill_contact_form(contact)
        self.submit_contact_creation()
        self.return_to_home_page()
        self.contact_cache = None

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        #select contact by index
        wd.find_elements_by_name("selected[]")[index].click()
        #delete contact
        wd.find_element_by_css_selector("input[value='Delete']").click()
        wd.switch_to_alert().accept()
        self.return_to_home_page()
        self.contact_cache = None

    def edit_first_contact(self):
        self.edit_contact_by_index(0)

    def edit_contact_by_index(self, index, edit_contact):
        wd = self.app.wd
        #edit contact
        wd.find_elements_by_xpath("//img[@src='icons/pencil.png']/parent::a")[index].click()
        self.fill_contact_form(edit_contact)
        #submit edition
        wd.find_element_by_xpath("//div[@id='content']/form[1]/input[22]").click()
        #return to home page
        wd.find_element_by_link_text("home page").click()
        self.contact_cache = None

    def count(self):
        wd = self.app.wd
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contacts_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.contact_cache = []
            for element in wd.find_elements_by_name("entry"):
                cells = element.find_elements_by_tag_name("td")
                cellLast = cells[1].text
                cellFirst = cells[2].text
                cellAddress = cells[3].text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                all_mails = cells[4].text
                all_phones = cells[5].text
                self.contact_cache.append(Contact(firstname= cellFirst, lastname = cellLast, id = id, address= cellAddress,
                                                  all_mails_from_home_page = all_mails,
                                                  all_phones_from_home_page = all_phones))
        return self.contact_cache

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.return_to_home_page()
        #open contact to edit
        wd.find_elements_by_xpath("//img[@src='icons/pencil.png']/parent::a")[index].click()

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")
        homephone = wd.find_element_by_name("home").get_attribute("value")
        mobilephone = wd.find_element_by_name("mobile").get_attribute("value")
        workphone = wd.find_element_by_name("work").get_attribute("value")
        phone2 = wd.find_element_by_name("phone2").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        return Contact (firstname=firstname, lastname=lastname, id=id, address=address,
                        homePhone=homephone, mobilePhone=mobilephone, workPhone=workphone, phone2=phone2,
                        email=email, email2=email2, email3=email3)

    def open_contact_view_page_by_index(self, index):
        wd = self.app.wd
        self.return_to_home_page()
        #open contact to detail
        wd.find_elements_by_xpath("//img[@src='icons/status_online.png']/parent::a")[index].click()


    def get_contacts_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_page_by_index(index)
        text = wd.find_element_by_id("content").text
        homephone = re.search("H: (.*)", text).group(1)
        mobilephone = re.search("M: (.*)", text).group(1)
        workphone = re.search("W: (.*)", text).group(1)
        phone2 = re.search("P: (.*)", text).group(1)
        return Contact (homePhone=homephone, mobilePhone=mobilephone, workPhone=workphone, phone2=phone2)

    def delete_contact_by_id(self, id):
        wd = self.app.wd
        #select contact by id
        wd.find_element_by_css_selector("input[value = '%s']" % id).click()
        #delete contact
        wd.find_element_by_css_selector("input[value='Delete']").click()
        wd.switch_to_alert().accept()
        self.return_to_home_page()
        self.contact_cache = None

    def edit_contact_by_id(self, id, edit_contact):
        wd = self.app.wd
        #edit contact
        #wd.find_elements_by_xpath("//img[@src='icons/pencil.png']/parent::a")[index].click()
        wd.get("http://localhost/addressbook/edit.php?id=%s" % id)
        self.fill_contact_form(edit_contact)
        #submit edition
        wd.find_element_by_xpath("//div[@id='content']/form[1]/input[22]").click()
        #return to home page
        wd.find_element_by_link_text("home page").click()
        self.contact_cache = None







