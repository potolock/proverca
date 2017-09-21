from selenium.webdriver.firefox.webdriver import WebDriver
from fixture.session import SessionHelper_group
from fixture.session import SessionHelper_contact
from fixture.group import GroupHelper_group


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


    def return_contact_page(self):
        wd = self.wd
        wd.find_element_by_link_text("home page").click()

    def submit(self):
        wd = self.wd
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.return_contact_page()

    def fill_new_contact(self, group):
        wd = self.wd
        self.open_contact_page()
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(group.firstname)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(group.lastname)
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(group.company)
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(group.address)
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(group.email)
        wd.find_element_by_name("homepage").click()
        wd.find_element_by_name("homepage").clear()
        wd.find_element_by_name("homepage").send_keys(group.homepage)

    def open_contact_page(self):
        wd = self.wd
        wd.find_element_by_link_text("add new").click()


    def open_page(self):
        wd = self.wd
        # open page
        wd.get("http://localhost:8080/addressbook/")

    def destroy (self):
        self.wd.quit()