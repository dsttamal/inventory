# Generated by Django 3.2.4 on 2021-06-30 07:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='clients',
            old_name='address',
            new_name='adress',
        ),
        migrations.RenameField(
            model_name='clients',
            old_name='phone',
            new_name='phn',
        ),
    ]
