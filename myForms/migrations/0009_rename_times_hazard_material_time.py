# Generated by Django 4.2 on 2023-05-18 23:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myForms', '0008_rename_time_hazard_material_times'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hazard_material',
            old_name='Times',
            new_name='Time',
        ),
    ]
