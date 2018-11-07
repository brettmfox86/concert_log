# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from concert_app.concert_log.models import Profile, UserConcert

# Create an instance of our MyAdminSite() class.  We will register models using this instead of 'admin.site'
admin_site = admin.site

# Register your models here.
admin_site.register(Profile)
admin_site.register(UserConcert)