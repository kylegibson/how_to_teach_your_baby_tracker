# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('words', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='WordGrouping',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='word',
            name='grouping',
            field=models.ForeignKey(related_name='words', blank=True, to='words.WordGrouping', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='word',
            name='views',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
