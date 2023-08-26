# Generated by Django 4.2.2 on 2023-07-31 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('connections', '0014_delete_loads'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='consumer',
            name='address',
        ),
        migrations.AddField(
            model_name='consumer',
            name='Lane',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='consumer',
            name='Road',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
