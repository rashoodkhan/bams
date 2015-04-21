from django.shortcuts import render
from models import ReportMetaData as RMD,ReportType
from survey.models import SurveyItem, Survey
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
		form = ItemForm()

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
	type_id = int(type_id)
	report_id = int(report_id)

	if request.method == "POST":
		form = None

		if report_id in [1,8]:
			form = PriorityForm(request.POST)

			if report_id is 1 and form.is_valid():
				no_priority = False
				building = int(request.POST["building"])
				try:
					priority = int(request.POST["priority"])
				except Exception:
					no_priority = True

				building = Building.objects.all().filter(id=building)[0]
				priority_all = Priority.objects.all()
				priority_chosen = None

				if no_priority is False:
					priority_chosen = priority_all.filter(id=priority)[0]

				survey = Survey.objects.all()
				survey_item = SurveyItem.objects.all()

				survey = survey.filter(building=building)[0]
				survey_item = survey_item.filter(survey=survey)


				if no_priority:
					context_dict = {'priorities':priority_all,
					                'title':'Action Reports by Priority',
					                'building':building}
					data = {}
					for p in priority_all:
						data[str(p.description)] = survey_item.filter(priority=p)

					context_dict['data'] = data
					return render(request,'reports/action_priority_display.html',context_dict)

				else:
					context_dict = {'priorities':priority_chosen,
					                'title':'Action Reports by Priority',
					                'building':building}
					data = {}
					data[str(priority_chosen.description)] = survey_item.filter(priority=priority_chosen)
					context_dict['data'] = data

					return render(request,'reports/action_priority_display.html',context_dict)

			if report_id is 8 and form.is_valid():
				pass


		elif report_id in [2,5]:
			form = ZoneForm(request.POST)
		elif report_id in [3,6]:
			form = BuildingForm(request.POST)
		elif report_id in [4,7]:
			form = ItemForm(request.POST)

		pass
	pass


