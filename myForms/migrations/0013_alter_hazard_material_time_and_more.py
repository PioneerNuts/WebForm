# Generated by Django 4.2 on 2023-04-28 20:38

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('myForms', '0012_alter_hazard_material_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hazard_material',
            name='Time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='metal_detection',
            name='Time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
