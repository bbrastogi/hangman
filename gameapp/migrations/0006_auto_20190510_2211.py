# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-05-10 16:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gameapp', '0005_gameapp_no_of_tries'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gameapp',
            name='no_of_tries',
        ),
        migrations.AddField(
            model_name='gameapp',
            name='alphabets',
            field=models.CharField(default='', max_length=30),
        ),
    ]
