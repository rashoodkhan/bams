# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='surveyitem',
            name='cost',
            field=models.DecimalField(max_digits=20, decimal_places=2, blank=True),
        ),
        migrations.AlterField(
            model_name='surveyitem',
            name='remarks',
            field=models.CharField(max_length=300, blank=True),
        ),
    ]
