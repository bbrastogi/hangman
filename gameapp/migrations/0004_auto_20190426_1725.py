# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-04-26 11:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gameapp', '0003_gameapp_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='gameapp',
            name='guessed',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='gameapp',
            name='wrong',
            field=models.CharField(default='', max_length=30),
        ),
    ]
