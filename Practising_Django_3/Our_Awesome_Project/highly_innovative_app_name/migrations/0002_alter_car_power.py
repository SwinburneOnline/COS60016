# Generated by Django 3.2.12 on 2022-04-07 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('highly_innovative_app_name', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='power',
            field=models.IntegerField(),
        ),
    ]
