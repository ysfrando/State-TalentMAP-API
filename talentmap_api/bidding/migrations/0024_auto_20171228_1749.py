# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-28 17:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bidding', '0023_merge_20171220_1954'),
    ]

    operations = [
        migrations.AddField(
            model_name='bid',
            name='is_priority',
            field=models.BooleanField(default=False, help_text="Flag indicating if this bid is the bidder's priority bid"),
        ),
        migrations.AddField(
            model_name='bid',
            name='panel_reschedule_count',
            field=models.IntegerField(default=0, help_text="The number of times this bid's panel date has been rescheduled"),
        ),
    ]
