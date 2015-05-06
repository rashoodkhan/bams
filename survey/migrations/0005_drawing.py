# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import survey.models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0004_auto_20150426_0402'),
    ]

    operations = [
        migrations.CreateModel(
            name='Drawing',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200, verbose_name=b'Drawing Name')),
                ('description', models.TextField(max_length=500, verbose_name=b'Drawing Description')),
                ('file', models.FileField(upload_to=survey.models.get_upload_path_rest, verbose_name=b'Drawing')),
                ('survey', models.ForeignKey(to='survey.Survey')),
            ],
        ),
    ]
