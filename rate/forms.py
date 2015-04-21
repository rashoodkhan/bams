__author__ = 'rashid'
from django.forms import ModelForm
from models import Rate
from codes.models import Type, ItemCode, FinishingCode, ActionCode, UnitOfMeasure

class RateForm(ModelForm):
	class Meta:
		model = Rate
		fields = ['name','type','item','finishing_code','action_code','unit','rate']

	def clean(self):
		cleaned_data = super(RateForm,self).clean()
		type = cleaned_data.get("type")
		item = cleaned_data.get("item")
		fc = cleaned_data.get("finishing_code")
		ac = cleaned_data.get("action_code")
		unit = cleaned_data.get("unit")

		type = Type.objects.filter(name=type)
		item = ItemCode.objects.filter(code=item)
		fc = FinishingCode.objects.filter(code=fc)
		ac = ActionCode.objects.filter(code=ac)
		unit = UnitOfMeasure.objects.filter(code=unit)

		if type is not None and item is not None and fc is not None and \
						ac is not None and unit is not None:


			rate = Rate.objects.filter(item=item,type=type,finishing_code=fc,action_code=ac,unit=unit)

			if len(rate) is not 0:
				msg = "The given rate has already been entered with given details"
				self.add_error('type',msg)
				self.add_error('item',msg)
				self.add_error('finishing_code',msg)
				self.add_error('action_code',msg)
				self.add_error('unit',msg)