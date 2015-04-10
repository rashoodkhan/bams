from django.shortcuts import render
from models import Survey,SurveyItem

def index(request):
	surveys = Survey.objects.all()
	return render(request,'survey/survey.html',{'data':surveys})
