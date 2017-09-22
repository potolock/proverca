

class GroupHelper_group:
      def __init__(self, app):
        self.app = app


      def return_to_group_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()

      def delete_first_group (self):
          wd = self.app.wd
          self.open_group_page()
          # select first group
          wd.find_element_by_name("selected[]").click()
          # submit delete
          wd.find_element_by_name("delete").click()
          self.return_to_group_page()



      def create(self, group):
        wd = self.app.wd
        self.open_group_page()
        # init group creation
        wd.find_element_by_name("new").click()
        # fill group form
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        # submit group creation
        wd.find_element_by_name("submit").click()
        self.return_to_group_page()

      def open_group_page(self):
         wd = self.app.wd
         # open group page
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





