# Generated by Django 4.1.3 on 2022-11-30 01:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_alter_salon_options_alumno_idsalon'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='alumno',
            constraint=models.UniqueConstraint(fields=('id', 'first_name', 'last_name'), name='primary_key_alumno'),
        ),
    ]