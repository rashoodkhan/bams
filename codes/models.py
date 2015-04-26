from django.db import models


class Priority(models.Model):
	code = models.CharField('Priority Code',max_length=20)
	description = models.CharField('Priority Description',max_length=300)

	def __str__(self):
		return self.code


class UnitOfMeasure(models.Model):
	code = models.CharField('Unit of Measure',max_length=20)
	description = models.CharField('Description',max_length=300)

	def __str__(self):
		return self.code

class ConstructionType(models.Model):
	name = models.CharField('Construction Type',max_length=300)

	def __str__(self):
		return self.name


class Site(models.Model):
	name = models.CharField('Site Name',max_length=300)

	def __str__(self):
		return self.name


class SiteGroup(models.Model):
	code = models.CharField('Site Code',max_length=30)
	description = models.CharField('Site Description',max_length=300)
	site = models.ForeignKey(Site,null=False)

	def __str__(self):
		return self.code


class BuildingType(models.Model):
	code = models.CharField('Building Code',max_length=30)
	description = models.CharField('Building Description',max_length=300)

	def __str__(self):
		return self.code

"""
	The model stores the building information.
"""
class Building(models.Model):
	route_seq = models.CharField('Route Sequence',max_length=30)
	title = models.CharField('Title',max_length=300)
	building_type = models.ForeignKey(BuildingType)
	construction_type = models.ForeignKey(ConstructionType)
	site_zone = models.ForeignKey(SiteGroup)
	remarks = models.CharField('Remarks',max_length=300)

	def __str__(self):
		return self.route_seq

"""
	Define the types of buildings.
	Currently two types of types exists, i.e. Internal or External.
	In future, more types can be added depending on the requirement of the projects
"""
class Type(models.Model):
	name = models.CharField('Type',max_length=30)

	def __str__(self):
		return self.name

class ItemCode(models.Model):
	type = models.ForeignKey(Type,null=False)
	code = models.CharField('Item Code',max_length=30)
	description = models.CharField('Item Description',max_length=300)
	specification = models.CharField('Item Specification',max_length=300)

	def __str__(self):
		return self.code

class SurfaceCode(models.Model):
	item = models.ForeignKey(ItemCode)
	code = models.CharField('Code',max_length=30)
	description = models.CharField('Description',max_length=300)

	def __str__(self):
		return self.code

class ActionCode(models.Model):
	item = models.ForeignKey(ItemCode)
	code = models.CharField('Code',max_length=30)
	description = models.CharField('Description',max_length=300)

	def __str__(self):
		return self.code

class SpecialRequirementCode(models.Model):
	item = models.ForeignKey(ItemCode)
	code = models.CharField('Code',max_length=30)
	description = models.CharField('Description',max_length=300)

	def __str__(self):
		return self.code

"""
Stores all the other Codes Models. So if a new model is added, the MetaData should be updated!
"""
class MetaDataInformation(models.Model):
	name = models.CharField(max_length=300)

	def __str__(self):
		return self.name

