# Generated by Django 4.2.5 on 2023-10-03 11:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travel_app', '0002_team'),
    ]

    operations = [
        migrations.RenameField(
            model_name='team',
            old_name='p_name',
            new_name='pname',
        ),
    ]