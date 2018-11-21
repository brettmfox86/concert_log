# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models
from django.db.models import FileField


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_photo = FileField(blank=True, null=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return '%s (%s)' % (self.user.username, self.user.id)


class UserConcert(models.Model):
    user = models.ForeignKey(User, related_name='user_userConcert', on_delete=models.CASCADE)
    concert_id = models.IntegerField()

    def __str__(self):
        return '%s (%s) - %s' % (self.user.username, self.user.id, str(self.concert_id))
