# Generated by Django 4.2 on 2023-04-18 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_team_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='playerprofile',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='Player_Profile'),
        ),
    ]