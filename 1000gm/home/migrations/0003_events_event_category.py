# Generated by Django 3.2.8 on 2023-04-18 05:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_ecategory'),
    ]

    operations = [
        migrations.AddField(
            model_name='events',
            name='event_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.ecategory'),
        ),
    ]