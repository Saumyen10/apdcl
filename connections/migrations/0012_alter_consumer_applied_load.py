# Generated by Django 4.2.2 on 2023-07-27 05:43

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('connections', '0011_alter_consumer_applied_load'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consumer',
            name='Applied_Load',
            field=models.FloatField(validators=[django.core.validators.MinValueValidator(0.1), django.core.validators.MaxValueValidator(25)]),
        ),
    ]
