# Generated by Django 4.2.2 on 2023-08-01 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('connections', '0017_alter_consumer_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='consumer',
            name='Father_Name',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='consumer',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
