
from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin
from django.db.models import signals
from django.dispatch import dispatcher


from misgastos import settings

class UserProfile(models.Model):
    user = models.ForeignKey(User, unique=True)
    number_months = models.IntegerField(default = settings.MONTH)
    def get_number_months(self):
        return range(0,self.number_months)
    def __unicode__(self):
        return self.user.username + "_profile"
admin.site.register(UserProfile)


def user_post_save(sender, instance, signal, *args, **kwargs):
    # Creates user profile
    profile, new = UserProfile.objects.get_or_create(user=instance)

signals.post_save.connect(user_post_save, sender=User)
