# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0003_remove_surveyitem_finishing_code'),
    ]

    operations = [
        migrations.RenameField(
            model_name='surveyitem',
            old_name='unit',
            new_name='damaged_unit',
        ),
        migrations.AddField(
            model_name='surveyitem',
            name='total_unit',
            field=models.IntegerField(default=0),
        ),
    ]
