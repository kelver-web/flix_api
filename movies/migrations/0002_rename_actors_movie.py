# Generated by Django 5.0.2 on 2024-03-03 14:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('actors', '0002_alter_actors_options_alter_actors_nationality'),
        ('genres', '0001_initial'),
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Actors',
            new_name='Movie',
        ),
    ]