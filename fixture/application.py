from selenium.webdriver.firefox.webdriver import WebDriver
from fixture.session import SessionHelper_group
from fixture.session import SessionHelper_contact
from fixture.group import GroupHelper_group
from fixture.group import GroupHelper_contact


class Application_group:

    def __init__(self):
        self.wd = WebDriver(capabilities={"marionette": False})
        self.wd.implicitly_wait(60)
        self.session = SessionHelper_group(self)
        self.group = GroupHelper_group (self)

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost:8080/addressbook/")

    def destroy (self):
        self.wd.quit()



class Application_contact:

    def __init__(self):
        self.wd = WebDriver(capabilities={"marionette": False})
        self.wd.implicitly_wait(60)
        self.session = SessionHelper_contact(self)
        self.group = GroupHelper_contact(self)

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost:8080/addressbook/")


    def destroy (self):
        self.wd.quit()