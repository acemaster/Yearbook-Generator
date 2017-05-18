import os
import re
import sys
from django.core.files import File

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'yearbook.settings')

import django
django.setup()

from main.models import *


def addstudent(name,rollno,section,img_dict):
	s = Student()
	s.rollno = rollno
	s.name = name
	s.section = section
	s.save()
	if s.rollno in img_dict:
		with open(img_dict[s.rollno][0], 'r') as f:
			image_file = File(f) 
			s.image.save(img_dict[s.rollno][1], image_file, True)
		s.save()


import csv
img_dict = {}
if len(sys.argv) == 2:
	images = os.listdir('/Users/acemaster/Downloads/Yearbook')
	for img in images:
		img_dict[img.split('.')[0]] = ['/Users/acemaster/Downloads/Yearbook/'+img,img]
	with open(sys.argv[1], 'rb') as csvfile:
		reader = csv.reader(csvfile)
		for row in reader:

			addstudent(row[0],row[1],row[2],img_dict) 