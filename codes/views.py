from django.shortcuts import render

from models import MetaDataInformation

def index(request):
	return render(request, 'codes/index.html',{})

def codes(request):
	meta_data = MetaDataInformation.objects.all()
	return render(request, 'codes/codes.html',{'data':meta_data})

def edit(request,code_id):
	pass

def add(request,code_id):
	pass
