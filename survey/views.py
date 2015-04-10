from django.http import HttpResponse
from django.shortcuts import render
from models import Survey,SurveyItem
from forms import SurveyForm
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
