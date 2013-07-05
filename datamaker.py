import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "vimusi.settings")

from django.contrib.auth.models import User
from core.models import UserProfile
from django.conf import settings
from teachers.models import TeacherProfile

DEFAULT_USERNAME = "tester"

def make_users(how_many_users):
    usernames = ['%s%d' % (DEFAULT_USERNAME, x) for x in range(0,how_many_users)]
    email = ['dave+%s%d@zenlab.com' % (DEFAULT_USERNAME, x) for x in range(0,how_many_users)]
    password = 'password'
    userset = dict(zip(usernames, email))
    print userset
    users = [User.objects.create_user(key, value, password) for key, value in userset.iteritems()]
    return users

def make_teachers():
    users = User.objects.filter(username__contains=DEFAULT_USERNAME)
    teachers = [TeacherProfile.objects.create(user = user, availability="Monday - Friday, 1PM to 6PM", about="I teach guitar and bass.") for user in users]
    [teacher.save() for teacher in teachers]
    return teachers

def make_user_profiles():
    users = User.objects.filter(username__contains=DEFAULT_USERNAME)
    user_profiles = [UserProfile.objects.create(user=user) for user in users]
    [user_profile.save() for user_profile in user_profiles]
    return user_profiles

if __name__ == '__main__':

    print 'Making users...'
    users = make_users(5)
    print users

    print 'Making user profiles...'
    user_profiles = make_user_profiles()
    print user_profiles

    print 'Making teachers...'
    teachers = make_teachers()
    print teachers