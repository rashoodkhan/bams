from django.shortcuts import render
from forms import *

from models import MetaDataInformation

def index(request):
	return render(request, 'codes/index.html',{})

def codes(request):
	meta_data = MetaDataInformation.objects.all()
	return render(request, 'codes/codes.html',{'data':meta_data})

def edit(request,code_id):
	pass

def add(request,code_id):
	code_id = int(code_id)
	print "Hello"
	print code_id
	result = None
	if code_id == 1:
		result = PriorityForm()
	elif code_id == 2:
		result = UnitOfMeasureForm()
	elif code_id == 3:
		result = ConstructionTypeForm()
	elif code_id == 4:
		result = SiteForm()
	elif code_id == 5:
		result = SiteGroupForm()
	elif code_id == 6:
		result = BuildingTypeForm()
	elif code_id == 7:
		result = BuildingCodeForm()
	elif code_id == 8:
		result = TypeForm()
	elif code_id == 9:
		result = ItemCodeForm()
	elif code_id == 10:
		result = FinishingCodeForm()
	elif code_id == 11:
		result = SurfaceCodeForm()
	elif code_id == 12:
		result = ActionCodeForm()
	elif code_id == 13:
		result = SpecialRequirementCodeForm()

	if result is None:
		print "RESULT IS NONE"
	try:
		title = MetaDataInformation.objects.all().filter(pk=code_id)[0].name
	except Exception:
		title = "Not Found"

	return render(request,'codes/add_form.html',{'form':result,'title':title})
