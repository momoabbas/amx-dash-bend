# Generated by Django 4.1.4 on 2022-12-14 15:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DronCount', '0006_alter_drone_next_maintainance_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='gmap',
            old_name='latitude',
            new_name='Lat',
        ),
        migrations.RenameField(
            model_name='gmap',
            old_name='longitude',
            new_name='Lng',
        ),
    ]
