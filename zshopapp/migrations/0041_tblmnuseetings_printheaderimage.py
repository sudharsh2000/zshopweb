# Generated by Django 4.2.7 on 2025-03-01 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zshopapp', '0040_tblmnuseetings_company'),
    ]

    operations = [
        migrations.AddField(
            model_name='tblmnuseetings',
            name='printheaderimage',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
