
class Group:

    def __init__(self, name=None, header=None, footer=None):
        self.name = name
        self.header = header
        self.footer = footer


class Contact:
    def __init__(self, firstname=None, lastname=None, company=None, address=None, email=None, homepage=None):
        self.firstname = firstname
        self.lastname = lastname
        self.company = company
        self.address = address
        self.email = email
        self.homepage = homepage
