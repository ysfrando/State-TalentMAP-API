# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-08 17:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bidding', '0008_auto_20170925_1910'),
    ]

    operations = [
        migrations.AddField(
            model_name='bidcycle',
            name='cycle_deadline_date',
            field=models.DateField(default='1900-01-01', help_text='The deadline date for the bid cycle'),
            preserve_default=False,
        ),
    ]