# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-19 18:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='in_print',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]
