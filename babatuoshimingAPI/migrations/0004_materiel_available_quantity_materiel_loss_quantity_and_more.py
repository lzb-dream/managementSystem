# Generated by Django 4.2.2 on 2023-08-19 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("babatuoshimingAPI", "0003_materiel_merchant"),
    ]

    operations = [
        migrations.AddField(
            model_name="materiel",
            name="available_quantity",
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name="materiel",
            name="loss_quantity",
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name="materiel",
            name="outbound_quantity",
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name="materiel",
            name="quantity_used",
            field=models.IntegerField(default=0),
        ),
    ]
