# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
def image_path(instance,filename):
    return '/'.join(['classimages',filename,])

class Student(models.Model):
    """
    Description: Student
    """
    rollno = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    section = models.CharField(max_length=100)
    image = models.ImageField(null=True,upload_to=image_path)
    def __unicode__(self):
    	return self.rollno


class Quote(models.Model):
    """
    Description: Quotes
    """
    student = models.ForeignKey(Student)
    quote = models.TextField()
    def __unicode__(self):
    	return self.student.rollno
