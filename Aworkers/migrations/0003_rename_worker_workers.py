# Generated by Django 4.0.4 on 2022-06-24 06:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Aworkers', '0002_worker_location'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='worker',
            new_name='Workers',
        ),
    ]