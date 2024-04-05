# Generated by Django 2.0.6 on 2018-07-12 19:45

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backoffice', '0008_humansrobot_gain'),
    ]

    operations = [
        migrations.AlterField(
            model_name='humansrobot',
            name='Gain',
            field=models.FloatField(validators=[django.core.validators.MaxValueValidator(200.0), django.core.validators.MinValueValidator(0.0)]),
        ),
    ]