# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-04-23 08:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gameapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gameapp',
            name='alphabet_key',
            field=models.CharField(max_length=250, null=True),
        ),
    ]
