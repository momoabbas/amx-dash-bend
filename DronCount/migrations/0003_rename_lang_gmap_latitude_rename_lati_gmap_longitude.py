# Generated by Django 4.0.5 on 2022-12-05 11:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DronCount', '0002_rename_log_review_log_logdata'),
    ]

    operations = [
        migrations.RenameField(
            model_name='gmap',
            old_name='lang',
            new_name='latitude',
        ),
        migrations.RenameField(
            model_name='gmap',
            old_name='lati',
            new_name='longitude',
        ),
    ]
