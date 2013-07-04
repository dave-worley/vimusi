from django.db import models
from teachers.models import TeacherProfile
from teachers.models import TeacherFile
from core.models import UserProfile


class ClassSession(models.Model):
    CLASS_SESSION_TYPES = (
        ('SINGLE', 'Single Student'),
        ('GROUP', 'Group Class'),
        ('ARCHIVE', 'Prerecorded Video'),
    )
    title = models.CharField(max_length=200)
    description = models.TextField()
    session_start = models.DateTimeField()
    session_end = models.DateTimeField()
    class_type = models.CharField(max_length=25, choices=CLASS_SESSION_TYPES)
    teacher = models.ForeignKey(TeacherProfile)
    students = models.ManyToManyField(UserProfile)
    files = models.ManyToManyField(TeacherFile, blank=True)
    fee = models.FloatField()

    def __unicode__(self):
        return self.title
