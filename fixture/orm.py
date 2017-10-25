from  datetime import datetime
from pony.orm import*

class ORMFixture:


    db = Database()


    class ORMGroup(db.Entity):
        _table_ = 'group_list'
        id = PrimaryKey(int, column='group_id')
        name = Optional(str, column='group_name')
        header = Optional(str, column='group_header')
        footer = Optional(str, column='group_footer')

    class ORMContact(db.Entity):
        _table_ = 'addressbook'
        id = PrimaryKey(int, column='id')
        firstname = Optional(str, column='firstname')
        lastname = Optional(str, column='lastname')
        deprecated = Optional(datetime, column='deprecated')


    def __init__(self, host, name, user, password):
        self.db._bind('mysql', host=host, database=name, user=user, password=password, autocommit=True)
        self.db.generate_mapping()

    @db_session
    def get_group_list(self):
        return list(select(g for g in ORMFixture.ORMGroup))