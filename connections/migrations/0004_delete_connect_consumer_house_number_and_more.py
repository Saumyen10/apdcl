# Generated by Django 4.2.2 on 2023-07-21 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('connections', '0003_rename_addressproof_consumer_address_proof_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='connect',
        ),
        migrations.AddField(
            model_name='consumer',
            name='House_Number',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='consumer',
            name='Mobile_Number',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]