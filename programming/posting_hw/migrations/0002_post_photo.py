# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-08 01:51
from __future__ import unicode_literals

from django.db import migrations, models
import posting_hw.models


class Migration(migrations.Migration):

    dependencies = [
        ('posting_hw', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='photo',
            field=models.ImageField(blank=True, upload_to=posting_hw.models.random_name_upload_to),
        ),
    ]
