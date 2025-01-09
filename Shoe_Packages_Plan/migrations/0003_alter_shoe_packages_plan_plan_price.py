# Generated by Django 5.0.6 on 2025-01-09 12:13

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shoe_Packages_Plan', '0002_alter_shoe_packages_plan_plan_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shoe_packages_plan',
            name='plan_price',
            field=models.IntegerField(blank=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(6)]),
        ),
    ]
