# Generated by Django 4.2.2 on 2023-08-01 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('connections', '0016_rename_lane_consumer_lane_rename_road_consumer_road_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consumer',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
