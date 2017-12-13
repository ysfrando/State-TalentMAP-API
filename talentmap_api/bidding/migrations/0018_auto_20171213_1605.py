# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-13 16:05
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bidding', '0017_auto_20171207_1529'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bid',
            options={'managed': True, 'ordering': ['bidcycle__cycle_start_date', 'update_date']},
        ),
        migrations.RemoveField(
            model_name='bid',
            name='submission_date',
        ),
        migrations.AddField(
            model_name='bid',
            name='approved_date',
            field=models.DateField(help_text='The date the bid was approved', null=True),
        ),
        migrations.AddField(
            model_name='bid',
            name='closed_date',
            field=models.DateField(help_text='The date the bid was closed', null=True),
        ),
        migrations.AddField(
            model_name='bid',
            name='create_date',
            field=models.DateField(auto_now_add=True, default=datetime.date(2017, 12, 13)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bid',
            name='declined_date',
            field=models.DateField(help_text='The date the bid was declined', null=True),
        ),
        migrations.AddField(
            model_name='bid',
            name='draft_date',
            field=models.DateField(auto_now_add=True, default=datetime.date(2017, 12, 13)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bid',
            name='handshake_accepted_date',
            field=models.DateField(help_text='The date the handshake was accepted', null=True),
        ),
        migrations.AddField(
            model_name='bid',
            name='handshake_offered_date',
            field=models.DateField(help_text='The date the handshake was offered', null=True),
        ),
        migrations.AddField(
            model_name='bid',
            name='in_panel_date',
            field=models.DateField(help_text='The date the bid was scheduled for panel', null=True),
        ),
        migrations.AddField(
            model_name='bid',
            name='scheduled_panel_date',
            field=models.DateField(help_text='The scheduled date for paneling', null=True),
        ),
        migrations.AddField(
            model_name='bid',
            name='submitted_date',
            field=models.DateField(help_text='The date the bid was submitted', null=True),
        ),
    ]
