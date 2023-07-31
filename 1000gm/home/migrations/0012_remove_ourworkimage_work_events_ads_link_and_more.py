# Generated by Django 4.2.2 on 2023-06-23 17:05

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0011_alter_scoholastic_active"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="ourworkimage",
            name="work",
        ),
        migrations.AddField(
            model_name="events",
            name="ads_link",
            field=models.CharField(blank=True, max_length=156, null=True),
        ),
        migrations.DeleteModel(
            name="OurWork",
        ),
        migrations.DeleteModel(
            name="OurWorkImage",
        ),
    ]
