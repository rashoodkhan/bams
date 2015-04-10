__author__ = 'rashid'
from django.forms import ModelForm
from models import Rate

class RateForm(ModelForm):
	class Meta:
		model = Rate
		fields = ['name','type','item','finishing_code','action_code','unit','rate']