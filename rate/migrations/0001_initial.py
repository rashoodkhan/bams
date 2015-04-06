# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('codes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rate', models.IntegerField(default=0)),
                ('name', models.CharField(max_length=30, verbose_name=b'Name')),
                ('action_code', models.ForeignKey(to='codes.ActionCode')),
                ('finishing_code', models.ForeignKey(to='codes.FinishingCode')),
                ('item', models.ForeignKey(to='codes.ItemCode')),
                ('type', models.ForeignKey(to='codes.Type')),
                ('unit', models.ForeignKey(to='codes.UnitOfMeasure')),
            ],
        ),
    ]
