# -*- coding: utf-8 -*-
# try something like 

def form():
    form = SQLFORM.factory(
        Field('your_name', requires=IS_NOT_EMPTY()),
        Field('join_date', type='date', requires=IS_DATE())
        Field('membership', requires=IS_IN_SET[('individual', 'company','family')] )
		)
    if form.process().accepted:
        response.flash = 'form accepted'
        session.your_name = form.vars.your_name
        session.join_date = form.vars.join_date
        session.membership = form.vars.membership
        redirect(URL("formaccepted"))
    elif form.errors:
        response.flash = 'form has error'
    return locals()

def formaccepted():
    return locals

def index(): return dict(message="hello from factory.py")



