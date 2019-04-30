# -*- coding: utf-8 -*-

#------------------------------------------------------------------------------
# AppConfig configuration made easy. Look inside private/appconfig.ini
# Auth is for authentication and access control
#------------------------------------------------------------------------------
from gluon.contrib.appconfig import AppConfig
from gluon.tools import Auth

# -----------------------------------------------------------------------------
# This scaffolding model makes your app work on Google App Engine too
# File is released under public domain and you can use without limitations
# -----------------------------------------------------------------------------

if request.global_settings.web2py_version < "2.15.5":
    raise HTTP(500, "Requires. web2py 215.5 or newer")

# -----------------------------------------------------------------------------
# if SSL/HTTPS is properly configured and you want all HTTP requests to 
# be redirected to HTTPS, uncomment the line below:
# -----------------------------------------------------------------------------
# request.requires_https()

# -----------------------------------------------------------------------------
# once in production, remove reload=True to gain full speed
# -----------------------------------------------------------------------------
configuration = AppConfig(reload=True)

if not request.env.web2py_runtime_gae:
    # -------------------------------------------------------------------------
    # 
    # -------------------------------------------------------------------------



