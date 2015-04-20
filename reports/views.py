from django.shortcuts import render
from models import ReportMetaData as RMD,ReportType
from forms import *

def index(request):
	types = ReportType.objects.all()
	action_type = types.filter(name="Action")[0]
	cost_type = types.filter(name="Cost")[0]
	survey_type = types.filter(name="Survey")[0]

	reports = RMD.objects.all()
	action_reports = reports.filter(type=action_type)
	cost_reports = reports.filter(type=cost_type)
	survey_reports = reports.filter(type=survey_type)

	return render(request,'reports/index.html',{
		'action_type':action_type,
	    'action_reports':action_reports,
	    'cost_type':cost_type,
	    'cost_reports':cost_reports,
	    'survey_type':survey_type,
	    'survey_reports':survey_reports,
	})

def getSurveyForm(request,type_id,report_id):
	type_id = int(type_id)
	report_id = int(report_id)
	report = RMD.objects.all().filter(id=report_id)[0]

	form = None

	#Actions Forms:-
	if report_id is 1:
		form = PriorityForm()
	elif report_id is 2:
		form = ZoneForm()
	elif report_id is 3:
		form = BuildingForm()
	elif report_id is 4:
		form = ItemForm

	#Cost Forms:-
	elif report_id is 5:
		form = ZoneForm()
	elif report_id is 6:
		form = BuildingForm()
	elif report_id is 7:
		form = ItemForm()
	elif report_id is 8:
		form = PriorityForm()

	return render(request,'reports/form.html',{'type_id':type_id,
	                                            'form':form,
	                                            'report_id':report_id,
	                                            'report':report})

def GenerateReport(request,type_id,report_id):
	pass