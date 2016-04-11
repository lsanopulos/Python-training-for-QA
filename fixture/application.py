from selenium import webdriver
from fixture.group import GroupHelper
from fixture.contacts import CreateContactHelper
from fixture.session import SessionHelper

class Application():
    def __init__(self, browser, baseUrl):
        if browser == "firefox":
            self.wd = webdriver.Firefox()
        elif browser == "chrome":
            self.wd = webdriver.Chrome()
        elif browser == "ie":
            self.wd = webdriver.Ie()
        else:
            raise ValueError("Unrecognized browser %s" % browser)

        self.session = SessionHelper(self)
        self.contacts = CreateContactHelper(self)
        self.group = GroupHelper(self)
        self.baseUrl = baseUrl

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False


    def open_home_page(self):
        wd = self.wd
        # open homepage
        if not (wd.current_url.endswith("addressbook/") and len(wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]")) > 0):
            wd.get(self.baseUrl)

    def destroy(self):
        self.wd.quit()