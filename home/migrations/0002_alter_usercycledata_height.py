# Generated by Django 5.1.2 on 2024-10-20 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usercycledata',
            name='height',
            field=models.FloatField(help_text='Enter your height in feet (e.g., 5.6 for 5 feet 6 inches).'),
        ),
    ]
