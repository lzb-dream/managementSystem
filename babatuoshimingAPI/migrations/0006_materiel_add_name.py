# Generated by Django 4.2.2 on 2023-08-24 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("babatuoshimingAPI", "0005_alter_users_status"),
    ]

    operations = [
        migrations.AddField(
            model_name="materiel",
            name="add_name",
            field=models.CharField(blank=True, max_length=200),
        ),
    ]