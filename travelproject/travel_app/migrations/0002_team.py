# Generated by Django 4.2.5 on 2023-10-03 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p_name', models.CharField(max_length=250)),
                ('image', models.ImageField(upload_to='pics')),
                ('des', models.TextField()),
            ],
        ),
    ]
