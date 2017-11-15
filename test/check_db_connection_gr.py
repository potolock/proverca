

from fixture.orm import ORMFixture
from model.group import Group, Contact


db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")

try:
    groups = db.get_group_list()
    for group in groups:
        print (group)
    print(len(groups))
finally:
    pass#db.destroy()



