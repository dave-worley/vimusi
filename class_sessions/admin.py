from django.contrib import admin
from .models import ClassSession

class ClassSessionAdmin(admin.ModelAdmin):
    pass
admin.site.register(ClassSession, ClassSessionAdmin)