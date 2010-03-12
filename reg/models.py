
from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin

class UserProfile(models.Model):
    user = models.ForeignKey(User, unique=True)
    number_months = models.IntegerField()
    def get_number_months(self):
        return range(0,self.numer_months)
    def __unicode__(self):
        return self.user.username + "_profile"
admin.site.register(UserProfile)
