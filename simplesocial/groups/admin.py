from django.contrib import admin
from . import models


# Register your models here.

class GroupMemberInline(admin.TabularInline):
    model = models.GroupMember
    fields = ['user','group']


admin.site.register(models.Group)
admin.site.register(models.GroupMember)