# Generated by Django 5.0.6 on 2025-01-15 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User_Profiles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_profiles',
            name='address_1',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='user_profiles',
            name='address_2',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='user_profiles',
            name='city',
            field=models.CharField(blank=True, max_length=60),
        ),
        migrations.AddField(
            model_name='user_profiles',
            name='country',
            field=models.CharField(blank=True, max_length=60),
        ),
        migrations.AddField(
            model_name='user_profiles',
            name='phone',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='user_profiles',
            name='state',
            field=models.CharField(blank=True, max_length=60),
        ),
        migrations.AddField(
            model_name='user_profiles',
            name='zip_code',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]
