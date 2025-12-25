from django.contrib import admin
from .models import *

# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message')

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('project_name', 'description')

admin.site.register(Project, ProjectAdmin)
admin.site.register(Contact, ContactAdmin) 