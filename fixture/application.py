from selenium import webdriver
from fixture.session import SessionHelper
from fixture.group import Helper_group
from fixture.group import Helper_contact


class Application:


    def __init__(self, browser, base_url):
        if browser == "firefox":
            self.wd = webdriver.Firefox(capabilities={"marionette": False}, executable_path="C:\SeleniumDrivers\geckodriver.exe")
        elif browser == "chrome":
            self.wd = webdriver.Chrome(executable_path="C:\SeleniumDrivers\chromedriver.exe")
        elif browser == "ie":
            self.wd = webdriver.Ie(executable_path="C:\SeleniumDrivers\IEDriverServer.exe")
        else:
            raise ValueError("Unrecognized browser %s" % browser)
        self.wd.implicitly_wait(0.5)
        self.session = SessionHelper(self)
        self.contact = Helper_contact(self)
        self.group = Helper_group (self)
        self.base_url = base_url

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def open_home_page(self):
        wd = self.wd
        wd.get(self.base_url)


    def destroy (self):
        self.wd.quit()




