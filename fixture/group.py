
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from model.group import Group, Contact
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class Helper_group:
     def __init__(self, app):
          self.app = app

     group_cache = None


     def get_group_list(self):
         if self.group_cache is None:
             wd = self.app.wd
             self.open_group_page()
             self.group_cache = []
             for element in wd.find_elements_by_css_selector("span.group"):
                 text = element.text
                 id = element.find_element_by_name("selected[]").get_attribute("value")
                 self.group_cache.append(Group(name=text, id=id))
         return list(self.group_cache)



     def count(self):
        wd = self.app.wd
        self.open_group_page()
        return len(wd.find_elements_by_name("selected[]"))


     def return_to_group_page(self):
         wd = self.app.wd
         wd.find_element_by_link_text("group page").click()

     def modify_first_group(self, new_group_data):
          wd = self.app.wd
          self.open_group_page()
          self.select_first_group()
          # open modification form
          wd.find_element_by_name("edit").click()
          # fill group form
          self.fill_group_form(new_group_data)
          # submit modification
          wd.find_element_by_name("update").click()
          self.return_to_group_page()
          self.group_cache = None


     def delete_first_group (self):
          wd = self.app.wd
          self.open_group_page()
          self.select_first_group()
          # submit delete
          wd.find_element_by_name("delete").click()
          self.return_to_group_page()
          self.group_cache = None


     def select_first_group(self):
          wd = self.app.wd
          wd.find_element_by_name("selected[]").click()


     def create(self, group):
         wd = self.app.wd
         self.open_group_page()
         # init group creation
         wd.find_element_by_name("new").click()
         self.fill_group_form(group)
         # submit group creation
         wd.find_element_by_name("submit").click()
         self.return_to_group_page()
         self.group_cache = None


     def fill_group_form(self, group):
         wd = self.app.wd
         self.change_field_value("group_name", group.name)
         self.change_field_value("group_header", group.header)
         self.change_field_value("group_footer", group.footer)


     def change_field_value(self, field_name, text):
         wd = self.app.wd
         if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

     def open_group_page(self):
         wd = self.app.wd
         if not (wd.current_url.endswith("group.php") and len (wd.find_elements_by_name("new")) > 0):
            wd.find_element_by_link_text("groups").click()




class Helper_contact:
    def __init__(self, app):
        self.app = app



    def get_contact_list(self):
        wd = self.app.wd
        contacts = []
        for el in wd.find_elements_by_xpath("//table[@id='maintable']/tbody/tr[@name='entry']"):
            text = el.text
            lastname = el.find_element_by_xpath("td[2]").text
            firstname = el.find_element_by_xpath("td[3]").text
            address = el.find_element_by_xpath("td[4]").text
            #email = el.find_element_by_xpath("td[5]/a").text
            #try:
                  #email = el.find_element_by_xpath("td[5]/a").text
            #except NoSuchElementException:
                #email = ""
            id = el.find_element_by_name("selected[]").get_attribute("value")
            contacts.append(Contact(firstname=firstname, lastname=lastname, address=address, id=id))
        return contacts

    def count(self):
        wd = self.app.wd
        self.open_contact_page()
        return len(wd.find_elements_by_name("selected[]"))


    def return_contact_page(self):
        wd = self.app.wd

        wd.find_element_by_link_text("home page").click()
    def modify_first_contact(self, new_contact_data):
        wd = self.app.wd
        wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr[2]/td[8]/a/img").click()
        # fill group form
        self.fill_contact_form(new_contact_data)
        # submit modification
        wd.find_element_by_name("update").click()
        self.return_contact_page()



    def submit(self):
        wd = self.app.wd
        wd.find_element_by_name("submit").click()
        self.return_contact_page()



    def delete_first_contact(self):
        wd = self.app.wd
        self.select_first_contact()
        # submit deletion
        wd.find_element_by_xpath("//*[@value='Delete']").click()
        # selecr action
        wd.switch_to_alert().accept()

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def fill_new(self, group):
        wd = self.app.wd
        self.open_contact_page()
        # init contact create
        wd.find_element_by_link_text("add new").click()
        self.fill_contact_form(group)
        # submit contact creation
        wd.find_element_by_name("submit").click()
        self.return_contact_page()


    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_field_contact_value("firstname", contact.firstname)
        self.change_field_contact_value("lastname", contact.lastname)
        self.change_field_contact_value("company", contact.company)
        self.change_field_contact_value("address", contact.address)
        self.change_field_contact_value("email", contact.email)
        self.change_field_contact_value("homepage", contact.homepage)



    def change_field_contact_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def open_contact_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("http://localhost:8080/addressbook/") and len (wd.find_elements_by_name("add")) > 0):
           wd.find_element_by_link_text("add new").click()







