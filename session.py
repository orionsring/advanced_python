# -*- coding: utf-8 -*- 
# try something like

def set():
    session.name="Sam";
    session.date="8/1/2015"
    session.membership="family"
    return locals()

def view():
    return locals()

