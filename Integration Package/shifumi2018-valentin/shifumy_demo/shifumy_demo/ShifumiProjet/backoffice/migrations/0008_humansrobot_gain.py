# Generated by Django 2.0.6 on 2018-07-12 19:38

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backoffice', '0007_auto_20180712_2008'),
    ]

    operations = [
        migrations.AddField(
            model_name='humansrobot',
            name='Gain',
            field=models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(200), django.core.validators.MinValueValidator(0)]),
            preserve_default=False,
        ),
    ]
