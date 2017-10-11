
from sys import maxsize



class Group:

    def __init__(self, name=None, header=None, footer=None, id=None):
        self.name = name
        self.header = header
        self.footer = footer
        self.id = id

    def __repr__(self):
        return "%s:%s" % (self.id, self.name)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.name == other.name

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize


class Contact:

    def __init__(self, firstname=None, lastname=None, id=None, all_phones_from_home_page=None, homephone=None, mobilephone=None, workphone=None, secondaryphone=None, address=None, company=None, email=None, homepage=None):
        self.firstname = firstname
        self.lastname = lastname
        self.address = address
        self.company = company
        self.email = email
        self.homepage = homepage
        self.homephone = homephone
        self.mobilephone = mobilephone
        self.workphone = workphone
        self.secondaryphone = secondaryphone
        self.id = id
        self.all_phones_from_home_page = all_phones_from_home_page

    def __repr__(self):
        return "%s:%s:%s:%s:%s:%s" % (self.id, self.firstname, self.lastname, self.homephone, self.all_phones_from_home_page, self.mobilephone, self.workphone, self.secondaryphone, self.address)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.firstname == other.firstname

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
