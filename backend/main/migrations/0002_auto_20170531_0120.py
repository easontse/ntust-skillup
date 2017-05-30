# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-30 17:20
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('pic_loc', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('price', models.FloatField()),
                ('posted_on', models.DateTimeField()),
                ('start_from', models.DateField()),
                ('end_on', models.DateField()),
                ('deadline', models.DateTimeField()),
                ('click_counter', models.IntegerField(default=0)),
                ('categories', models.ManyToManyField(to='main.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('good_at', models.ManyToManyField(to='main.Category')),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Wish',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('content', models.CharField(max_length=100)),
                ('posted_on', models.DateTimeField()),
                ('click_counter', models.IntegerField(default=0)),
                ('categories', models.ManyToManyField(to='main.Category')),
                ('posted_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='interest',
            name='user',
        ),
        migrations.DeleteModel(
            name='Interest',
        ),
        migrations.AddField(
            model_name='lesson',
            name='hosted_by',
            field=models.ManyToManyField(to='main.Teacher'),
        ),
        migrations.AddField(
            model_name='member',
            name='interested_in',
            field=models.ManyToManyField(to='main.Category'),
        ),
        migrations.AddField(
            model_name='member',
            name='lessons_joint',
            field=models.ManyToManyField(to='main.Lesson'),
        ),
    ]