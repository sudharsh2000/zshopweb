# Generated by Django 4.2.7 on 2024-09-25 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zshopapp', '0025_alter_tblcomplaintdetails_imei_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='tblcomplaintdetails',
            name='company',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
