# Generated by Django 4.1.3 on 2023-04-22 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_football', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='score',
            field=models.CharField(max_length=10),
        ),
    ]