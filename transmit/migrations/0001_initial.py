# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Files',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('file_name', models.CharField(max_length=300)),
                ('file_path', models.CharField(max_length=300)),
                ('times_played', models.IntegerField(null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
