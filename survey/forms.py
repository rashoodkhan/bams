__author__ = 'rashid'
from django.forms import ModelForm
from codes.models import *
from models import *

class SurveyForm(ModelForm):
	class Meta:
		model = Survey
		fields = ['building','elevation','type']