# Generated by Django 2.0.4 on 2019-06-10 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bidding', '0015_auto_20190521_1347'),
    ]

    operations = [
        migrations.AddField(
            model_name='cycleposition',
            name='posted_date',
            field=models.DateTimeField(help_text='The created date for the cycle positon', null=True),
        ),
    ]