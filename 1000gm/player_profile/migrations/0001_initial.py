# Generated by Django 3.2 on 2023-06-23 06:01

from django.db import migrations


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('home', '0008_scoholastic'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlayerProfileProxy',
            fields=[
            ],
            options={
                'verbose_name': 'Player Profile',
                'verbose_name_plural': 'Player Profile',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('home.playerprofile',),
        ),
        migrations.CreateModel(
            name='PlayerProfileVideoProxy',
            fields=[
            ],
            options={
                'verbose_name': 'Player Videos',
                'verbose_name_plural': 'Player Videos',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('home.playerprofilevideo',),
        ),
    ]