# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from main.models import *

# Register your models here.
class StudentAdmin(admin.ModelAdmin):
	search_fields = ['rollno','name']

class StudentTwoAdmin(admin.ModelAdmin):
	search_fields = ['student__rollno','student__name']

admin.site.register(Student,StudentAdmin)
admin.site.register(Quote,StudentTwoAdmin)
