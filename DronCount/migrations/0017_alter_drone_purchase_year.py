# Generated by Django 4.1.4 on 2022-12-20 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("DronCount", "0016_alter_drone_purchase_year"),
    ]

    operations = [
        migrations.AlterField(
            model_name="drone",
            name="purchase_year",
            field=models.DateTimeField(
                auto_now_add=True, null=True, verbose_name="Created_Timestamp"
            ),
        ),
    ]
