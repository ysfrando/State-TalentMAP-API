# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-14 17:42
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0010_auto_20170905_1512'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sharable',
            name='receiving_user',
        ),
        migrations.RemoveField(
            model_name='sharable',
            name='sharing_user',
        ),
        migrations.DeleteModel(
            name='Sharable',
        ),
    ]