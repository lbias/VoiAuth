# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-20 11:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_remove_speakermodel_sample'),
    ]

    operations = [
        migrations.AddField(
            model_name='speakermodel',
            name='audio',
            field=models.FileField(default=0, upload_to=b''),
            preserve_default=False,
        ),
    ]
