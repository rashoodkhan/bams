from django.http import HttpResponse
from django.shortcuts import render
from forms import *

from models import MetaDataInformation

def index(request):
	return render(request, 'codes/index.html',{})

def codes(request):
	meta_data = MetaDataInformation.objects.all()
	return render(request, 'codes/codes.html',{'data':meta_data})

def edit(request,code_id):
	code_id = int(code_id)
	results = None
	try:
		title = MetaDataInformation.objects.all().filter(pk=code_id)[0].name
	except Exception:
		title = "Not Found"

	"""
	Some models do not have description, hence the choice is used.
	If choice is 1 => Description field is present
	If choice is 2 => Name field is present
	If choice is 3 => Route Seq has to be displayed

	By default, choice is 1
	"""
	choice = 1

	if code_id == 1:
		results = Priority.objects.all()

	elif code_id == 2:
		results = UnitOfMeasure.objects.all()

	elif code_id == 3:
		results = ConstructionType.objects.all()
		choice = 2

	elif code_id == 4:
		results = Site.objects.all()
		choice = 2

	elif code_id == 5:
		results = SiteGroup.objects.all()

	elif code_id == 6:
		results = BuildingType.objects.all()

	elif code_id == 7:
		results = Building.objects.all()
		choice = 3

	elif code_id == 8:
		results = Type.objects.all()
		choice = 2

	elif code_id == 9:
		results = ItemCode.objects.all()

	elif code_id == 10:
		results = FinishingCode.objects.all()

	elif code_id == 12:
		results = ActionCode.objects.all()

	elif code_id == 13:
		results = SpecialRequirementCode.objects.all()

	return render(request,'codes/codes_edit.html',{'data':results,'title':title,'code_id':code_id,'choice':choice})

def add(request,code_id):
	code_id = int(code_id)
	result = None

	try:
		title = MetaDataInformation.objects.all().filter(pk=code_id)[0].name
	except Exception:
		title = "Not Found"

	#If the form is submitted the below code adds it to the database
	if request.method == "POST":
		form = None
		if code_id == 1:
			form = PriorityForm(request.POST)

		elif code_id == 2:
			form = UnitOfMeasureForm(request.POST)

		elif code_id == 3:
			form =ConstructionTypeForm(request.POST)

		elif code_id == 4:
			form = SiteForm(request.POST)

		elif code_id == 5:
			form = SiteGroupForm(request.POST)

		elif code_id == 6:
			form = BuildingTypeForm(request.POST)

		elif code_id == 7:
			form = BuildingCodeForm(request.POST)

		elif code_id == 8:
			form = TypeForm(request.POST)

		elif code_id == 9:
			form = ItemCodeForm(request.POST)

		elif code_id == 10:
			form = FinishingCodeForm(request.POST)

		elif code_id == 11:
			form = SurfaceCodeForm(request.POST)

		elif code_id == 12:
			form = ActionCodeForm(request.POST)

		elif code_id == 13:
			form = SpecialRequirementCodeForm(request.POST)

		if form.is_valid():
			form.save(commit=True)
			return render(request,'codes/add_success.html',{'title':title})

	#In case the post method is not sent, the usual form has to be rendered
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

	return render(request,'codes/add_form.html',{'form':result,'title':title})
