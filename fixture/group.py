

class GroupHelper_group:
      def __init__(self, app):
        self.app = app


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

      def delete_first_group (self):
          wd = self.app.wd
          self.open_group_page()
          self.select_first_group()
          # submit delete
          wd.find_element_by_name("delete").click()
          self.return_to_group_page()


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
         wd.find_element_by_link_text("groups").click()


class GroupHelper_contact:
    def __init__(self, app):
        self.app = app


    def return_contact_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home page").click()

    def submit(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.return_contact_page()



    def delete_first_contact(self):
        wd = self.app.wd
        # select first contact
        wd.find_element_by_name("selected[]").click()
        # submit deletion
        wd.find_element_by_xpath("//*[@value='Delete']").click()
        # selecr action
        wd.switch_to_alert().accept()


    def fill_new(self, group):
        wd = self.app.wd
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
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()







