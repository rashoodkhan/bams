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

	def pp(self):
		return self.getRoute() + " " + self.getElevation() + " " + self.getType()

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
	remarks = models.CharField(max_length=300,blank=True)
	cost = models.DecimalField(max_digits=20,decimal_places=2,blank=True)

	def __str__(self):
		return self.survey.__str__() + " :: " + self.item.code

	def getItem(self):
		return self.item.description

	def getFinishingCode(self):
		codes = ""
		for x in self.finishing_code:
			codes = codes + " " + str(x)
		return codes

	def getCondition(self):
		codes = ""
		for x in self.condition:
			codes = codes + " " + str(x)
		return codes

	def getAction(self):
		return self.action.code

	def getUOM(self):
		return self.uom.code

	def getSpecialReq(self):
		return self.special_requirement.code

	def getPriority(self):
		return self.priority.description

	def getFinishingDescription(self):
		finishing_codes = FinishingCode.objects.filter(code__in = self.finishing_code)
		result = ""
		for code in finishing_codes:
			result = result + " " + code.description
		return result

	def getConditionDescription(self):
		codes = ""
		for x in self.condition:
			codes = codes + " " + str(x.description)
		return codes

	def getActionDescription(self):
		return self.action.description

	def getSpecialReqDescription(self):
		return self.special_requirement.description

	def getElevation(self):
		return self.survey.elevation

	def getRoute(self):
		return self.survey.building.route_seq




