# Generated by Django 4.1.4 on 2022-12-26 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("DronCount", "0018_alter_drone_next_maintainance_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="drone",
            name="Next_maintainance",
            field=models.DateTimeField(
                blank=True, null=True, verbose_name="Next_maintainance"
            ),
        ),
        migrations.AlterField(
            model_name="drone",
            name="purchase_year",
            field=models.DateTimeField(
                blank=True, null=True, verbose_name="purchase_year"
            ),
        ),
    ]
