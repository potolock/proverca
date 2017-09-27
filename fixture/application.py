from selenium.webdriver.firefox.webdriver import WebDriver
from fixture.session import SessionHelper
from fixture.group import Helper_group
from fixture.group import Helper_contact


class Application:


    def __init__(self):
        self.wd = WebDriver(capabilities={"marionette": False})
        self.wd.implicitly_wait(5)
        self.session = SessionHelper(self)
        self.contact = Helper_contact(self)
        self.group = Helper_group (self)

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost:8080/addressbook/")


    def destroy (self):
        self.wd.quit()




