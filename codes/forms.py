__author__ = 'rashid'
from models import *
from django.forms import ModelForm

class PriorityForm(ModelForm):
	class Meta:
		model = Priority
		fields = ['code','description']

class UnitOfMeasureForm(ModelForm):
	class Meta:
		model = UnitOfMeasure
		fields = ['code','description']

class ConstructionTypeForm(ModelForm):
	class Meta:
		model = ConstructionType
		fields = ['name']

class SiteForm(ModelForm):
	class Meta:
		model = Site
		fields = ['name']

class SiteGroupForm(ModelForm):
	class Meta:
		model = SiteGroup
		fields = ['code','description','site']

class BuildingTypeForm(ModelForm):
	class Meta:
		model = BuildingType
		fields = ['code','description']

class BuildingCodeForm(ModelForm):
	class Meta:
		model = Building
		fields = ['route_seq','title','building_type','construction_type','site_zone','remarks']

class TypeForm(ModelForm):
	class Meta:
		model = Type
		fields = ['name']

class ItemCodeForm(ModelForm):
	class Meta:
		model = ItemCode
		fields = ['type','code','description','specification']

class FinishingCodeForm(ModelForm):
	class Meta:
		model = FinishingCode
		fields = ['item','code','description']

class SurfaceCodeForm(ModelForm):
	class Meta:
		model = SurfaceCode
		fields = ['item','code','description']

class ActionCodeForm(ModelForm):
	class Meta:
		model = ActionCode
		fields = ['item','code','description']

class SpecialRequirementCodeForm(ModelForm):
	class Meta:
		model = SpecialRequirementCode
		fields = ['item','code','description']