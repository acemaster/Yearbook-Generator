import os
import re
import sys

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'yearbook.settings')

import django
django.setup()

from main.models import *

total_count = 0
def addquote(rollno,quote):
	q = Quote.objects.filter(student__rollno = rollno)
	if len(q) == 0:
		try:
			s = Student.objects.get(rollno = rollno)
			q = Quote()
			q.student = s
			q.quote = quote
			q.save()
			total_count = total_count + 1
		except Exception as e:
			print str(e)
	else:
		print "Already there"

import xlrd

book = xlrd.open_workbook(sys.argv[1])
fsheet = book.sheet_by_index(0)
i = 1
while True:
	try:
		print ('%.2f' % (fsheet.cell(i,2).value,)).rstrip('0').rstrip('.')
		print fsheet.cell(i,3).value
		print "============"
		if fsheet.cell(i,2).value or fsheet.cell(i,2).value!='':
			addquote(('%.2f' % (fsheet.cell(i,2).value,)).rstrip('0').rstrip('.'),fsheet.cell(i,3).value)
			print ""
		else:
			break
	except Exception as e:
		print "except" + str(e)
		break
	i = i + 1

print "Total added ", total_count
