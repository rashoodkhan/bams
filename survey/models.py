from django.db import models
from django.contrib.postgres.fields import ArrayField
from codes.models import *

class Survey(models.Model):
	building = models.ForeignKey(Building)
	elevation = models.CharField(max_length=300)
	type = models.ForeignKey(Type)

	def __str__(self):
		return self.building.route_seq + " :: " + self.elevation + " :: " + self.type.name

	def getRoute(self):
		return self.building.route_seq

	def getType(self):
		return self.type.name

	def getElevation(self):
		return self.elevation

class SurveyItem(models.Model):
	survey = models.ForeignKey(Survey)
	item = models.ForeignKey(ItemCode)
	finishing_code = ArrayField(models.CharField(max_length=100))
	condition = ArrayField(models.CharField(max_length=100))
	action = models.ForeignKey(ActionCode)
	unit = models.IntegerField(default=0)
	uom = models.ForeignKey(UnitOfMeasure)
	special_requirement = models.ForeignKey(SpecialRequirementCode)
	priority = models.ForeignKey(Priority)
	remarks = models.CharField(max_length=300)
	cost = models.DecimalField(max_digits=20,decimal_places=2)

	def __str__(self):
		return self.survey.__str__() + " :: " + self.item.code
