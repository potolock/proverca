

from model.group import Contact
import random
import string
import os.path
import json
import getopt
import sys



try:
     opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contact", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 6
f = "data/contact.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + ""*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])




testdata = [ Contact(firstname="", lastname="", company="", address="", email="", homepage="")] + [
            Contact(firstname=random_string("firstname", 10), lastname=random_string("lastname", 15),
                    company=random_string("company", 10), address=random_string("address", 20),
                      email=random_string("email", 10), homepage=random_string("homepage", 10))
    for i in range(n)
]


file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as f:
    f.write(json.dumps(testdata, default = lambda x: x.__dict__, indent=2))