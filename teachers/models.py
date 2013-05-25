from django.db import models
from django.contrib.auth.models import User

def sample_path_handler(instance, filename):
    return u"{username}/sample/".format(username = instance.user.username)

class TeacherProfile(models.Model):
    user = models.ForeignKey(User, unique = True)
    availability = models.CharField(max_length = 200)
    about = models.TextField(blank = True)
    audio_sample = models.FileField(upload_to = sample_path_handler, blank = True)
    profile_picture = models.FileField(upload_to = sample_path_handler, blank = True)
    profile_video = models.FileField(upload_to = sample_path_handler, blank = True)
    def __unicode__(self):
        return self.user.username
    def get_absolute_url(self):
        return "/members/%s/" % self.user.username
