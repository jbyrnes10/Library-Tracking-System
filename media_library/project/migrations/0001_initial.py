# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-06-20 18:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MediaHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_out', models.DateField()),
                ('date_due', models.DateField()),
                ('date_returned', models.DateField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='MediaItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=10)),
                ('title', models.CharField(max_length=100)),
                ('isbn', models.CharField(max_length=17)),
                ('author', models.CharField(max_length=100)),
                ('image_file', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Topics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=20, unique=True)),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='mediaitem',
            name='subtopic',
            field=models.ManyToManyField(related_name='subtopic_fk', to='project.Topics'),
        ),
        migrations.AddField(
            model_name='mediaitem',
            name='topic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='topic_fk', to='project.Topics'),
        ),
        migrations.AddField(
            model_name='mediahistory',
            name='borrower',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.User'),
        ),
        migrations.AddField(
            model_name='mediahistory',
            name='media_item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.MediaItem'),
        ),
    ]
