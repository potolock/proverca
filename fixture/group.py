
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

     def modify_group_by_index(self, index, new_group_data):
          wd = self.app.wd
          self.open_group_page()
          self.select_group_by_index(index)
          # open modification form
          wd.find_element_by_name("edit").click()
          # fill group form
          self.fill_group_form(new_group_data)
          # submit modification
          wd.find_element_by_name("update").click()
          self.return_to_group_page()
          self.group_cache = None

     def modify_first_group(self, new_group_data):
         self.modify_group_by_index(0)


     def select_group_by_index(self, index):
         wd = self.app.wd
         wd.find_elements_by_name("selected[]")[index].click()


     def delete_group_by_index (self, index):
          wd = self.app.wd
          self.open_group_page()
          self.select_group_by_index(index)
          # submit delete
          wd.find_element_by_name("delete").click()
          self.return_to_group_page()
          self.group_cache = None

     def delete_first_group(self):
         self.delete_group_by_index (0)

     # def delete_first_group (self):
     #      wd = self.app.wd
     #      self.open_group_page()
     #      self.select_first_group()
     #      # submit delete
     #      wd.find_element_by_name("delete").click()
     #      self.return_to_group_page()
     #      self.group_cache = None


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

    contact_cache = None

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        # открываем форму редактирования (index)po zadannomy indecsy
        self.open_contact_to_edit_by_index(index)
        # i iz etoy formy chitaem informaciy
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        homephone = wd.find_element_by_name("home").get_attribute("value")
        mobilephone = wd.find_element_by_name("mobile").get_attribute("value")
        workphone = wd.find_element_by_name("work").get_attribute("value")
        secondaryphone = wd.find_element_by_name("phone2").get_attribute("value")
        # teper iz etih dannyh stroim ob'ect
        return Contact(firstname=firstname, lastname=lastname, id=id, homephone=homephone, mobilephone=mobilephone,
                       workphone=workphone, secondaryphone=secondaryphone)

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.contact_cache = []
            for el in wd.find_elements_by_xpath("//table[@id='maintable']/tbody/tr[@name='entry']"):
                text = el.text
                lastname = el.find_element_by_xpath("td[2]").text
                firstname = el.find_element_by_xpath("td[3]").text
                id = el.find_element_by_name("selected[]").get_attribute("value")
                all_phones = el.find_element_by_xpath("td[6]").text.splitlines()
                self.contact_cache.append(Contact(firstname=firstname, lastname=lastname, id=id, homephone=all_phones[0], mobilephone=all_phones[1], workphone=all_phones[2], secondaryphone=all_phones[3]))
        return list(self.contact_cache)


    # def get_contact_list(self):
    #     if self.contact_cache is None:
    #         wd = self.app.wd
    #         self.app.open_home_page()
    #         self.contact_cache = []
    #         for row in wd.find_elements_by_name("entry"):
    #             cells = row.find_elements_by_tag_name("td")
    #             firstname = cells[1].text
    #             lastname = cells[2].text
    #             id = cells[0].find_element_by_tag_name("input").get_attribute("value")
    #             all_phones = cells[5].text.splitlines()
    #             self.contact_cache.append(Contact(firstname=firstname, lastname = lastname, id = id, homephone=all_phones[0], mobilephone=all_phones[1], workphone=all_phones[2], secondaryphone=all_phones[3]))
    #     return list (self.contact_cache)



    def count(self):
        wd = self.app.wd
        self.return_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    def return_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()

    def modify_contact_by_index(self, index, new_contact_data):
        wd = self.app.wd
        wd.find_elements_by_xpath("//table[@id='maintable']/tbody/tr/td[8]/a/img")[index].click()
        # fill group form
        self.fill_contact_form(new_contact_data)
        # submit modification
        wd.find_element_by_name("update").click()
        self.return_home_page()
        self.contact_cache = None

    def modify_first_contact(self, new_contact_data):
        self.modify_contact_by_index(0)

    def submit(self):
        wd = self.app.wd
        wd.find_element_by_name("submit").click()
        self.return_home_page()

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def delete_contact_by_index (self, index):
        wd = self.app.wd
        self.select_contact_by_index(index)
        wd.find_element_by_xpath("//*[@value='Delete']").click()
        wd.switch_to_alert().accept()
        self.contact_cache = None


    # def delete_first_contact(self):
    #     wd = self.app.wd
    #     self.select_first_contact()
    #     # submit deletion
    #     wd.find_element_by_xpath("//*[@value='Delete']").click()
    #     # selecr action
    #     wd.switch_to_alert().accept()
    #     self.contact_cache = None

    def select_first_contact(self):
        self.delete_contact_by_index(0)

    def fill_new(self, group):
        wd = self.app.wd
        self.return_home_page()
        # init contact create
        wd.find_element_by_link_text("add new").click()
        self.fill_contact_form(group)
        # submit contact creation
        wd.find_element_by_name("submit").click()
        self.return_home_page()
        self.contact_cache = None


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

    def open_edit_page(self):
        wd = self.app.wd
        if (wd.current_url.endswith("http://localhost:8080/addressbook/") and (len(wd.find_element_by_name("to_group")) > 0)):
            wd.find_element_by_link_text("add new").click()







