from model.contact import Contact
from selenium.webdriver.firefox.webdriver import WebDriver
from fixture.session_contact import SessionContactHelper
from fixture.create_contact import CreateContactHelper


class Application_contact():
    def __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
        self.session_contact = SessionContactHelper(self)
        self.create_contact = CreateContactHelper(self)

    def open_home_page(self):
        wd = self.wd
        # open home page
        wd.get("http://localhost/addressbook/")

    def destroy_contact(self):
        self.wd.quit()

