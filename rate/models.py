from django.db import models
from codes.models import Type,ItemCode,FinishingCode,ActionCode,UnitOfMeasure

class Rate(models.Model):
	type = models.ForeignKey(Type)
	item = models.ForeignKey(ItemCode)
	finishing_code = models.ForeignKey(FinishingCode)
	action_code = models.ForeignKey(ActionCode)
	unit = models.ForeignKey(UnitOfMeasure)
	rate = models.IntegerField(default=0)
	name = models.CharField("Name",max_length=30)

	def __str__(self):
		return self.name
