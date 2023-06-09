# Generated by Django 4.1.3 on 2023-04-23 02:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_football', '0002_alter_match_score'),
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('age', models.IntegerField(max_length=10)),
                ('nationality', models.CharField(max_length=50)),
                ('playing_club', models.CharField(max_length=50)),
            ],
        ),
    ]
