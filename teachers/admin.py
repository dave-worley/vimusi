from django.contrib import admin
from .models import TeacherProfile

class TeacherProfileAdmin(admin.ModelAdmin):
    pass
admin.site.register(TeacherProfile, TeacherProfileAdmin)
