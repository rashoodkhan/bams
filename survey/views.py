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
		form = SurveyItemForm(request.POST)
		if form.is_valid():
			survey_data = form.save(commit=False)
			building = Survey.objects.all().filter(pk=building_id)[0]
			survey_data.survey = building
			survey_data.cost = 0.0


			surface_states = form.cleaned_data['conditions']
			s_codes = []
			for s in surface_states:
				s_codes.append(str(s.code))

			survey_data.condition = s_codes

			survey_data.save()
			survey_items = SurveyItem.objects.all().filter(survey=building)
			return render(request,'survey/building_survey.html',{'survey':building,'data':survey_items,'success_added':1})
		else:
			return render(request,'survey/survey_data_form.html',{'form':form})
	form = SurveyItemForm()
	return render(request,'survey/survey_data_form.html',{'form':form})

def edit_building_data(request,building_id,survey_id):
	survey = SurveyItem.objects.all().filter(pk=survey_id)[0]
	if request.method == "POST":
		form = SurveyItemForm(request.POST,instance=survey)
		if form.is_valid():
			survey_data = form.save(commit=False)
			building = Survey.objects.all().filter(pk=building_id)[0]
			survey_data.survey = building
			survey_data.cost = 0.0

			finish_codes = form.cleaned_data['types']
			f_codes = []
			for f in finish_codes:
				f_codes.append(str(f.code))

			surface_states = form.cleaned_data['conditions']
			s_codes = []
			for s in surface_states:
				s_codes.append(str(s.code))

			survey_data.finishing_code = f_codes
			survey_data.condition = s_codes

			survey_data.save()
			survey_items = SurveyItem.objects.all().filter(survey=building)
			return render(request,'survey/building_survey.html',{'survey':building,'data':survey_items,'success_edited':1})
		else:
			return render(request,'survey/survey_data_form.html',{'form':form})

	f_codes = survey.finishing_code
	s_codes = survey.condition
	form = SurveyItemForm(instance=survey,initial={'types':f_codes,'conditions':s_codes})
	return render(request,'survey/survey_data_form.html',{'form':form,'edit_data':1})
