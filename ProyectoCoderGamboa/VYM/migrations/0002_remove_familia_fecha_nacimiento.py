# Generated by Django 4.1.2 on 2022-11-16 23:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('VYM', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='familia',
            name='fecha_nacimiento',
        ),
    ]
