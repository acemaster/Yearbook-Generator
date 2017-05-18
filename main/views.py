# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from main.models import *

# Create your views here.
def home(request):
	quotes = Quote.objects.all().order_by('student__name')
	response = {}
	response['quotes'] = quotes
	return render(request,'main/site/page.djt',response)