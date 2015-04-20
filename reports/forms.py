__author__ = 'rashid'

from django import forms
from codes.models import Building, Site, Type, Priority, ItemCode

priority_text = "Choose the priority. If nothing is chosen, all priorities are queried"
building_text = "Required Field - Pelase Select the building"
type_text = "Choose the type of building, If nothing is chosen, all types are queried"
item_text = "Required Field - Please select the item code"

class PriorityForm(forms.ModelForm):
	building = forms.ModelChoiceField(queryset=Building.objects.all(),required=True,help_text=building_text)
	priority = forms.ChoiceField(choices=Priority.objects.all(),required=False,help_text=priority_text)

class ZoneForm(forms.ModelForm):
	zone = forms.ModelChoiceField(queryset=Site.objects.all(),required=True)
	priority = forms.ChoiceField(choices=Priority.objects.all(),required=False,help_text=priority_text)

class BuildingForm(forms.ModelForm):
	building = forms.ModelChoiceField(queryset=Building.objects.all(),required=True,help_text=building_text)
	type = forms.ModelChoiceField(queryset=Type.objects.all(),required=False,help_text=type_text)
	priority = forms.ModelChoiceField(queryset=Priority.objects.al(),required=False,help_text=priority_text)

class ItemForm(forms.ModelForm):
	item = forms.ModelChoiceField(queryset=ItemCode.objects.all(),required=True,help_text=item_text)
	type = forms.ModelChoiceField(queryset=Type.objects.all(),required=False,help_text=type_text)
	priority = forms.ModelChoiceField(queryset=Priority.objects.al(),required=False,help_text=priority_text)


