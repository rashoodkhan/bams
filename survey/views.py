from django.http import HttpResponse
from django.shortcuts import render
from models import Survey,SurveyItem
from forms import SurveyForm, SurveyItemForm
def index(request):
	surveys = Survey.objects.all()
	return render(request,'survey/survey.html',{'data':surveys})

def add_survey(request):
	if request.method == "POST":
		form = SurveyForm(request.POST)
		if form.is_valid():
			form.save(commit=True)
			data = Survey.objects.all()
			return render(request,'survey/survey.html',{
				'data':data,
			    'success_added':1
			})
		else:
			return render(request,'survey/survey_form.html',{'form':form,'error':1})

	form = SurveyForm()
	return render(request,'survey/survey_form.html',{'form':form})

def building_survey(request,building_id):
	survey = Survey.objects.all().filter(pk=building_id)
	survey_items = SurveyItem.objects.all().filter(survey=survey)

	return render(request,'survey/building_survey.html',{'survey':survey[0],'data':survey_items})

def add_building_data(request,building_id):
	if request.method == "POST":
		#DO POST Related stuff
		pass
	form = SurveyItemForm()
	return render(request,'survey/survey_data_form.html',{'form':form})
