

from model.group import Contact
import random
import string


constant = [
    Contact(firstname="firstname1", lastname="lastname1", company="company1", address="address1", email="email1", homepage="homepage1"),
    Contact(firstname="firstname2", lastname="lastname2", company="company2", address="address2", email="email2", homepage="homepage2")

]

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + ""*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])




testdata = [ Contact(firstname="", lastname="", company="", address="", email="", homepage="")] + [
            Contact(firstname=random_string("firstname", 10), lastname=random_string("lastname", 15),
                    company=random_string("company", 10), address=random_string("address", 20),
                      email=random_string("email", 10), homepage=random_string("homepage", 10))
    for i in range(5)
]