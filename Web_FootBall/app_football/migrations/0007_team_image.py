# Generated by Django 4.1.3 on 2023-05-22 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_football', '0006_league_team_delete_match_delete_player'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
