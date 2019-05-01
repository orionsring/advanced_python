# -*- coding: utf-8 -*-
# try something like

def add():
    form = SQLFORM(db.contacts.process)
    return locals()

def view():
    if request.args(0) is None:
        return

def index(): return dict(message="hello from contacts.py")

def data():
    rows = db(db.contacts).select()
    return locals()

def filter():
    # get count
    rows_count = db(db.contacts).count()
    # get all records. sorted by name
    rows2_all_sorted_by_name = db(db.contacts).select(orderby=~db.contacts.last_name |
                                                      db.contacts.first_name)
    # filter, show only those whose last_name starts with M
    rows3_startswith = \
db(db.contacts.last_name.startswith('M')).select(orderby=db.contacts.state_name |
                                                 db.contacts.last_name)
    # filter, only show those from california
    rows4_by_state = db(~(db.contacts.state_name=='CA')).select(orderby=db.contacts.last_name | db.contacts.first_name)
    # boolean logic: & (and); | (or)
    rows5_combo = db((db.contacts.state_name=='CA') & 
(db.contacts.last_name.startswith('A'))).select(orderby=db.contacts.last_name)
    return locals()
