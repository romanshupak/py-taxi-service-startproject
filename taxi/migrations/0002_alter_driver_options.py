# Generated by Django 5.0.3 on 2024-03-26 10:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("taxi", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="driver",
            options={"ordering": ("license_number",)},
        ),
    ]
