from selenium.webdriver.firefox.webdriver import WebDriver
from fixture.group import GroupHelper
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
        if not (wd.current_url.endswith("addressbook/") and len(wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]")) > 0):
            wd.get("http://localhost/addressbook/")

    def destroy(self):
        self.wd.quit()