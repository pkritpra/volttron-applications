# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-20 18:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vtn', '0037_report'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='site',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='vtn.Site'),
        ),
        migrations.AlterField(
            model_name='report',
            name='report_request_id',
            field=models.CharField(blank=True, max_length=100, null=True, unique=True),
        ),
    ]
