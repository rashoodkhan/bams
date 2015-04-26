# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rate', '0002_remove_rate_finishing_code'),
        ('codes', '0002_metadatainformation'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='finishingcode',
            name='item',
        ),
        migrations.DeleteModel(
            name='FinishingCode',
        ),
    ]
