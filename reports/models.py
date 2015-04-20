from django.db import models

class ReportType(models.Model):
	name = models.CharField(max_length=200)

	def __str__(self):
		return self.name

class ReportMetaData(models.Model):
	name = models.CharField(max_length=200)
	type = models.ForeignKey(ReportType,null=True)

	def __str__(self):
		return self.type.name+" :: "+self.name