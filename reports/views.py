from django.shortcuts import render
from models import ReportMetaData as RMD,ReportType

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