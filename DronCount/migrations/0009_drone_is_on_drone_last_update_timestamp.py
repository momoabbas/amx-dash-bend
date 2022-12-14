# Generated by Django 4.1.4 on 2022-12-14 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DronCount', '0008_remove_drone_drone_location_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='drone',
            name='is_on',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='drone',
            name='last_update_timestamp',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='last_update_timestamp'),
        ),
    ]
