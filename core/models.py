from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.ForeignKey(User)
    about = models.TextField()
    def __unicode__(self):
        return "%s (%s)" % (self.user.username, self.user.email)

