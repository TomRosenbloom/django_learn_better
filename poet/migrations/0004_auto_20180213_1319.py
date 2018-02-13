# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-13 13:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0001_initial'),
        ('poet', '0003_auto_20180213_0941'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='poet',
            name='id',
        ),
        migrations.AddField(
            model_name='poet',
            name='person_ptr',
            field=models.OneToOneField(auto_created=True, default=0, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='person.Person'),
            preserve_default=False,
        ),
    ]
