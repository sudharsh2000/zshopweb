# Generated by Django 4.2.7 on 2024-12-05 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zshopapp', '0033_tblbusinessissue_discperc_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tbltransactionreceipt',
            name='pbill',
            field=models.ImageField(upload_to=None),
        ),
    ]
