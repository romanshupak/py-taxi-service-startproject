# Generated by Django 5.0.3 on 2024-03-26 17:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("taxi", "0003_alter_car_options"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="driver",
            options={"verbose_name": "user", "verbose_name_plural": "users"},
        ),
    ]