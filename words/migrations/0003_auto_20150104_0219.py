# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('words', '0002_auto_20150101_2118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='word',
            name='word',
            field=models.CharField(unique=True, max_length=255),
            preserve_default=True,
        ),
    ]
