# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.CharField(max_length=200)),
                ('price', models.DecimalField(null=True, max_digits=50, decimal_places=2)),
                ('date', models.DateField(null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('distance', models.DecimalField(null=True, max_digits=50, decimal_places=2)),
                ('duration', models.TimeField(null=True)),
                ('mood', models.CharField(max_length=50, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
