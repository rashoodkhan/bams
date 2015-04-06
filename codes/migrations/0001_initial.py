# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ActionCode',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(max_length=30, verbose_name=b'Code')),
                ('description', models.CharField(max_length=300, verbose_name=b'Description')),
            ],
        ),
        migrations.CreateModel(
            name='Building',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('route_seq', models.CharField(max_length=30, verbose_name=b'Route Sequence')),
                ('title', models.CharField(max_length=300, verbose_name=b'Title')),
                ('remarks', models.CharField(max_length=300, verbose_name=b'Remarks')),
            ],
        ),
        migrations.CreateModel(
            name='BuildingType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(max_length=30, verbose_name=b'Building Code')),
                ('description', models.CharField(max_length=300, verbose_name=b'Building Description')),
            ],
        ),
        migrations.CreateModel(
            name='ConstructionType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=300, verbose_name=b'Construction Type')),
            ],
        ),
        migrations.CreateModel(
            name='FinishingCode',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(max_length=30, verbose_name=b'Code')),
                ('description', models.CharField(max_length=300, verbose_name=b'Description')),
            ],
        ),
        migrations.CreateModel(
            name='ItemCode',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(max_length=30, verbose_name=b'Item Code')),
                ('description', models.CharField(max_length=300, verbose_name=b'Item Description')),
                ('specification', models.CharField(max_length=300, verbose_name=b'Item Specification')),
            ],
        ),
        migrations.CreateModel(
            name='Priority',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(max_length=20, verbose_name=b'Priority Code')),
                ('description', models.CharField(max_length=300, verbose_name=b'Priority Description')),
            ],
        ),
        migrations.CreateModel(
            name='Site',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=300, verbose_name=b'Site Name')),
            ],
        ),
        migrations.CreateModel(
            name='SiteGroup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(max_length=30, verbose_name=b'Site Code')),
                ('description', models.CharField(max_length=300, verbose_name=b'Site Description')),
                ('site', models.ForeignKey(to='codes.Site')),
            ],
        ),
        migrations.CreateModel(
            name='SpecialRequirementCode',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(max_length=30, verbose_name=b'Code')),
                ('description', models.CharField(max_length=300, verbose_name=b'Description')),
                ('item', models.ForeignKey(to='codes.ItemCode')),
            ],
        ),
        migrations.CreateModel(
            name='SurfaceCode',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(max_length=30, verbose_name=b'Code')),
                ('description', models.CharField(max_length=300, verbose_name=b'Description')),
                ('item', models.ForeignKey(to='codes.ItemCode')),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30, verbose_name=b'Type')),
            ],
        ),
        migrations.CreateModel(
            name='UnitOfMeasure',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(max_length=20, verbose_name=b'Unit of Measure')),
                ('description', models.CharField(max_length=300, verbose_name=b'Description')),
            ],
        ),
        migrations.AddField(
            model_name='itemcode',
            name='type',
            field=models.ForeignKey(to='codes.Type'),
        ),
        migrations.AddField(
            model_name='finishingcode',
            name='item',
            field=models.ForeignKey(to='codes.ItemCode'),
        ),
        migrations.AddField(
            model_name='building',
            name='building_type',
            field=models.ForeignKey(to='codes.BuildingType'),
        ),
        migrations.AddField(
            model_name='building',
            name='construction_type',
            field=models.ForeignKey(to='codes.ConstructionType'),
        ),
        migrations.AddField(
            model_name='building',
            name='site_zone',
            field=models.ForeignKey(to='codes.SiteGroup'),
        ),
        migrations.AddField(
            model_name='actioncode',
            name='item',
            field=models.ForeignKey(to='codes.ItemCode'),
        ),
    ]
