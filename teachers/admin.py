from django.contrib import admin
from .models import TeacherProfile, TeacherFile

class TeacherProfileAdmin(admin.ModelAdmin):
    pass
admin.site.register(TeacherProfile, TeacherProfileAdmin)

class TeacherFileAdmin(admin.ModelAdmin):
    pass
admin.site.register(TeacherFile, TeacherFileAdmin)