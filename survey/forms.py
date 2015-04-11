__author__ = 'rashid'
from django.forms import ModelForm, ValidationError
from django import forms
from codes.models import *
from codes.models import Building,Type

from models import *

class SurveyForm(ModelForm):
	class Meta:
		model = Survey
		fields = ['building','elevation','type']

	def clean(self):
		cleaned_data = super(SurveyForm,self).clean()
		building = cleaned_data.get("building")
		elevation = cleaned_data.get("elevation")
		type = cleaned_data.get("type")

		bObj = Building.objects.all().filter(route_seq=building)
		tObj = Type.objects.all().filter(name=type)

		if bObj is not None and tObj is not None:
			print "Reached here"
			bObj = bObj[0]
			tObj = tObj[0]

			survey = Survey.objects.all().filter(building=bObj,type=tObj,elevation=elevation)
			print len(survey)

			if len(survey) is not 0:
				msg = "The given building has already been entered with given details"
				self.add_error('building',msg)
				self.add_error('elevation',msg)
				self.add_error('type',msg)

class SurveyItemForm(ModelForm):
	types = forms.ModelMultipleChoiceField(queryset=FinishingCode.objects.all())
	conditions = forms.ModelMultipleChoiceField(queryset=SurfaceCode.objects.all())

	class Meta:
		model = SurveyItem
		fields = ['item','action','unit','uom','special_requirement','priority','remarks']

