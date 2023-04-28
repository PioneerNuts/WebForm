# Generated by Django 4.2 on 2023-04-07 20:43

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('myForms', '0002_test'),
    ]

    operations = [
        migrations.CreateModel(
            name='form2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sh_wallnut', models.CharField(max_length=50)),
                ('Desc', models.CharField(max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='test',
        ),
        migrations.AlterField(
            model_name='form1',
            name='Time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
