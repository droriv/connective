# Generated by Django 3.1.11 on 2021-06-24 07:22

import django.core.validators
from django.db import migrations, models
import server.utils.model_fields


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20210624_1022'),
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='has_summary',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='event',
            name='slug',
            field=models.CharField(default=server.utils.model_fields.random_slug, max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='summary_children_behavior',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)]),
        ),
        migrations.AddField(
            model_name='event',
            name='summary_general_notes',
            field=models.CharField(blank=True, max_length=400, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='summary_general_rating',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)]),
        ),
        migrations.AlterField(
            model_name='event',
            name='consumers',
            field=models.ManyToManyField(blank=True, to='users.Consumer'),
        ),
    ]