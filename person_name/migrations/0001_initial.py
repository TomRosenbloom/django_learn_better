# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-12 22:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mononym',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(choices=[('LEGAL', 'Legal'), ('MARITAL', 'Marital'), ('MAIDEN', 'Maiden'), ('PREFERRED', 'Preferred'), ('SOUBRIQUET', 'Soubriquet'), ('PSEUDONYM', 'Pseudonym')], max_length=20)),
                ('mononym', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Pictonym',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(choices=[('LEGAL', 'Legal'), ('MARITAL', 'Marital'), ('MAIDEN', 'Maiden'), ('PREFERRED', 'Preferred'), ('SOUBRIQUET', 'Soubriquet'), ('PSEUDONYM', 'Pseudonym')], max_length=20)),
                ('url', models.URLField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('description', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Polynym',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(choices=[('LEGAL', 'Legal'), ('MARITAL', 'Marital'), ('MAIDEN', 'Maiden'), ('PREFERRED', 'Preferred'), ('SOUBRIQUET', 'Soubriquet'), ('PSEUDONYM', 'Pseudonym')], max_length=20)),
                ('given', models.CharField(blank=True, max_length=50, null=True)),
                ('middle', models.CharField(blank=True, max_length=50, null=True)),
                ('moniker', models.CharField(blank=True, max_length=50, null=True)),
                ('surname', models.CharField(max_length=50)),
                ('generation', models.CharField(blank=True, choices=[('JUNIOR', 'Junior'), ('SENIOR', 'Senior')], max_length=10)),
                ('secondary_surname', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
