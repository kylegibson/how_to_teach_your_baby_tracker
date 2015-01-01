# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Word',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('word', models.CharField(max_length=255)),
                ('date_retired', models.DateTimeField(null=True, blank=True)),
                ('date_active', models.DateTimeField(null=True, blank=True)),
                ('views', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
