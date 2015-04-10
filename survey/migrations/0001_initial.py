# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.postgres.fields


class Migration(migrations.Migration):

    dependencies = [
        ('codes', '0002_metadatainformation'),
    ]

    operations = [
        migrations.CreateModel(
            name='Survey',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('elevation', models.CharField(max_length=300)),
                ('building', models.ForeignKey(to='codes.Building')),
                ('type', models.ForeignKey(to='codes.Type')),
            ],
        ),
        migrations.CreateModel(
            name='SurveyItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('finishing_code', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=100), size=None)),
                ('condition', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=100), size=None)),
                ('unit', models.IntegerField(default=0)),
                ('remarks', models.CharField(max_length=300)),
                ('cost', models.DecimalField(max_digits=20, decimal_places=2)),
                ('action', models.ForeignKey(to='codes.ActionCode')),
                ('item', models.ForeignKey(to='codes.ItemCode')),
                ('priority', models.ForeignKey(to='codes.Priority')),
                ('special_requirement', models.ForeignKey(to='codes.SpecialRequirementCode')),
                ('survey', models.ForeignKey(to='survey.Survey')),
                ('uom', models.ForeignKey(to='codes.UnitOfMeasure')),
            ],
        ),
    ]
