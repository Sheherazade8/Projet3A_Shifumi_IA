# Generated by Django 2.0.6 on 2018-06-06 11:31

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backoffice', '0002_auto_20180606_1330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='humans',
            name='humanOne',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(3), django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='humans',
            name='humanTwo',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(3), django.core.validators.MinValueValidator(1)]),
        ),
    ]
