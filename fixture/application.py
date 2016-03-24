from selenium.webdriver.firefox.webdriver import WebDriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper
from model.contact import Contact
from fixture.create_contact import CreateContactHelper
from fixture.session import SessionHelper

class Application():
    def __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
        self.session = SessionHelper(self)
        self.create_contact = CreateContactHelper(self)

    def open_home_page(self):
        wd = self.wd
        # open homepage
        wd.get("http://localhost/addressbook/")

    def destroy(self):
        self.wd.quit()