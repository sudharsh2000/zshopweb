# Generated by Django 4.2.7 on 2024-02-23 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zshopapp', '0002_tblitemmaster_os'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tbluserdetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userid', models.IntegerField(blank=True, null=True)),
                ('username', models.CharField(blank=True, max_length=50, null=True)),
                ('upassword', models.CharField(blank=True, max_length=50, null=True)),
                ('ugroup', models.IntegerField(blank=True, null=True)),
                ('astatus', models.IntegerField(blank=True, null=True)),
                ('company', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
    ]
