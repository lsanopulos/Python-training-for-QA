from selenium.webdriver.firefox.webdriver import WebDriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper
from model.contact import Contact
from fixture.contacts import CreateContactHelper
from fixture.session import SessionHelper

class Application():
    def __init__(self):
        self.wd = WebDriver()
        self.session = SessionHelper(self)
        self.contacts = CreateContactHelper(self)
        self.group = GroupHelper(self)

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False


    def open_home_page(self):
        wd = self.wd
        # open homepage
        wd.get("http://localhost/addressbook/")

    def destroy(self):
        self.wd.quit()