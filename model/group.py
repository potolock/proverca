
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

    def __init__(self, firstname=None, lastname=None, company=None, address=None, email=None, homepage=None, id=None):
        self.firstname = firstname
        self.lastname = lastname
        self.company = company
        self.address = address
        self.homepage = homepage
        self.email = email
        self.id = id

    def __repr__(self):
        return "%s:%s" % (self.id, self.email)

    def __eq__(self, other):
        return  (self.id is None or other.id is None or self.id == other.id) and self.email == other.email

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
