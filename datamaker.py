import os
from datetime import datetime, timedelta

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "vimusi.settings")

from django.contrib.auth.models import User
from core.models import UserProfile
from class_sessions.models import ClassSession
from teachers.models import TeacherProfile

DEFAULT_USERNAME = "tester"


def make_users(how_many_users):
    usernames = ['%s%d' % (DEFAULT_USERNAME, x) for x in range(0, how_many_users)]
    email = ['dave+%s%d@zenlab.com' % (DEFAULT_USERNAME, x) for x in range(0, how_many_users)]
    password = 'password'
    userset = dict(zip(usernames, email))
    print userset
    users = [User.objects.create_user(key, value, password) for key, value in userset.iteritems()]
    return users


def make_teachers():
    users = User.objects.filter(username__contains=DEFAULT_USERNAME)
    teachers = [TeacherProfile.objects.create(user=user, availability="Monday - Friday, 1PM to 6PM",
                                              about="I teach guitar and bass.") for user in users]
    [teacher.save() for teacher in teachers]
    return teachers


def make_user_profiles():
    users = User.objects.filter(username__contains=DEFAULT_USERNAME)
    user_profiles = [UserProfile.objects.create(user=user) for user in users]
    [user_profile.save() for user_profile in user_profiles]
    return user_profiles


def make_class_session(teacher, **options):
    options['teacher'] = teacher
    return ClassSession.objects.create(**options)


def make_class_sessions():
    teachers = TeacherProfile.objects.filter(user__username__contains=DEFAULT_USERNAME)
    student = UserProfile.objects.get(id=1)
    session_options = {}
    session_options['title'] = "Something Guitar Class"
    session_options['fee'] = 60
    session_options['session_start'] = datetime.now()
    session_options['session_end'] = datetime.now() + timedelta(hours=1)
    session_options['class_type'] = "SINGLE"
    sessions = [make_class_session(teacher, **session_options) for teacher in teachers]
    [session.students.add(student) for session in sessions]
    [session.save() for session in sessions]
    return sessions


if __name__ == '__main__':
    # print 'Making users...'
    # users = make_users(5)
    # print users
    #
    # print 'Making user profiles...'
    # user_profiles = make_user_profiles()
    # print user_profiles
    #
    # print 'Making teachers...'
    # teachers = make_teachers()
    # print teachers
    print 'Making class sessions...'
    sessions = make_class_sessions()
    print sessions