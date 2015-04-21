from django.shortcuts import render
from models import ReportMetaData as RMD,ReportType
from survey.models import SurveyItem, Survey, Site, SiteGroup
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
				#IMPLEMENT COST REPORT FOR PRIORITY
				pass


		elif report_id in [2,5]:
			form = ZoneForm(request.POST)

			if report_id is 2 and form.is_valid():
				no_priority = False
				priority_chosen = None
				zone = int(request.POST["zone"])
				try:
					priority = int(request.POST["priority"])
				except Exception:
					no_priority = True

				site = Site.objects.all().filter(id=zone)[0]
				site_zone = SiteGroup.objects.all().filter(site=site)

				wanted_buildings = set()

				"""
					Mother of Loops!
					Nested four for loops! Going deep and deep to get the data ;)

					P.S - Don't try to calculate the complexity. It works like a charm!
					Or at least I think it does work like a charm!
				"""
				for s in site_zone:
					buildings_temp = Building.objects.filter(site_zone=s)
					for b in buildings_temp:
						wanted_buildings.add(b.id)

				buildings = Building.objects.filter(pk__in = wanted_buildings)

				if no_priority:
					context_dict = {'title':'Actions Report by Zone',
					                'buildings':buildings,
					                'site':site}

					data = {}
					for b in buildings:
						surveys_temp = Survey.objects.filter(building=b)
						wanted_surveys = set()
						for survey in surveys_temp:
							survey_items = SurveyItem.objects.filter(survey=survey)
							for item in survey_items:
								wanted_surveys.add(item.id)
						survey_items = SurveyItem.objects.filter(pk__in = wanted_surveys)
						data[str(b.route_seq)] = survey_items
						print survey_items
					context_dict['data'] = data

					return render(request,'reports/action_zone_display.html',context_dict)
				else:
					priority_chosen = Priority.objects.filter(id=priority)[0]
					context_dict = {'title':'Actions Report by Zone',
					                'buildings':buildings,
					                'site':site,
					                'priority':priority_chosen}

					data = {}
					for b in buildings:
						surveys_temp = Survey.objects.filter(building=b)
						wanted_surveys = set()
						for survey in surveys_temp:
							survey_items = SurveyItem.objects.filter(survey=survey)
							for item in survey_items:
								wanted_surveys.add(item.id)
						survey_items = SurveyItem.objects.filter(pk__in = wanted_surveys)
						survey_items = survey_items.filter(priority=priority_chosen)
						data[str(b.route_seq)] = survey_items
						print survey_items
					context_dict['data'] = data

					return render(request,'reports/action_zone_display.html',context_dict)


		elif report_id in [3,6]:
			form = BuildingForm(request.POST)

			if report_id is 3 and form.is_valid():
				no_type = False
				no_priority = False
				building = int(request.POST["building"])
				try:
					type = int(request.POST["type"])
				except Exception:
					no_type = True

				try:
					priority = int(request.POST["priority"])
				except Exception:
					no_priority = True

				building = Building.objects.filter(id=building)[0]

				if no_priority and no_type:
					survey = Survey.objects.filter(building=building)
					wanted_surveys = set()

					for s in survey:
						survey_items = SurveyItem.objects.filter(survey=s)
						for si in survey_items:
							wanted_surveys.add(si.id)

					survey_items = SurveyItem.objects.filter(pk__in = wanted_surveys)

					context_dict = {'title':'Actions Report By Building',
					                'building':building,
					                'survey':survey,
					                'survey_items':survey_items}

					return render(request,'reports/action_building_display.html',context_dict)

				if no_type is False and no_priority is False:
					type_chosen = Type.objects.filter(pk=type)
					priority_chosen = Priority.objects.filter(pk=priority)
					survey = Survey.objects.filter(building=building,type=type_chosen)
					wanted_surveys = set()

					for s in survey:
						survey_items = SurveyItem.objects.filter(survey=s,priority=priority_chosen)
						for si in survey_items:
							wanted_surveys.add(si.id)

					survey_items = SurveyItem.objects.filter(pk__in = wanted_surveys)

					context_dict = {'title':'Actions Report By Building',
					                'building':building,
					                'survey':survey,
					                'survey_items':survey_items,
					                'type':type_chosen[0].name,
					                'priority':priority_chosen[0].description}

					return render(request,'reports/action_building_display.html',context_dict)


		elif report_id in [4,7]:
			form = ItemForm(request.POST)

		pass
	pass


