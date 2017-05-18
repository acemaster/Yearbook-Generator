import os
import re
import sys
from django.core.files import File

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'yearbook.settings')

import django
django.setup()

from main.models import *

def check():
	pics = os.listdir('/Users/acemaster/Downloads/SectionB')
	img_dict = {}
	for p in pics:
		rollno = p.split('.')[0].split(" ")[0]
		if len(rollno) < 2:
			rollno = "0"+rollno
		rollno = "1372" + rollno
		img_dict[rollno] = ['/Users/acemaster/Downloads/SectionB/'+p,p]
	count_of_no_filled = 0
	no_filled = []
	students = Student.objects.all()
	for s in students:
		if not s.image:
			if s.rollno in img_dict:
				with open(img_dict[s.rollno][0], 'r') as f:
					image_file = File(f) 
					s.image.save(img_dict[s.rollno][1], image_file, True)
				s.save()
				print s.rollno + " got image"
			else:
				count_of_no_filled = count_of_no_filled + 1
				no_filled.append(s)
	return no_filled,count_of_no_filled

def check_noquote():
	f = open('quotes.txt','r')
	q_list = f.readlines()
	i = 0
	students = Student.objects.all()
	for s in students:
		if len(Quote.objects.filter(student=s)) > 0:
			print s.rollno + " has quote"
		else:
			if s.image:
				q = Quote()
				q.student = s
				q.quote = q_list[i]
				q.save()
				print s.rollno + " " + s.name + " : "+ q_list[i]
				i = i+1


no_filled,count_of_no_filled = check()
print count_of_no_filled
for n in no_filled:
	print n.rollno + " " + n.name
check_noquote()