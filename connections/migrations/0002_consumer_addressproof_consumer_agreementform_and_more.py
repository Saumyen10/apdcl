# Generated by Django 4.2.2 on 2023-07-20 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('connections', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='consumer',
            name='addressproof',
            field=models.FileField(blank=True, null=True, upload_to='pdfs/'),
        ),
        migrations.AddField(
            model_name='consumer',
            name='agreementform',
            field=models.FileField(blank=True, null=True, upload_to='pdfs/'),
        ),
        migrations.AddField(
            model_name='consumer',
            name='identityproof',
            field=models.FileField(blank=True, null=True, upload_to='pdfs/'),
        ),
        migrations.AddField(
            model_name='consumer',
            name='passport',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='consumer',
            name='testreport',
            field=models.FileField(blank=True, null=True, upload_to='pdfs/'),
        ),
    ]
