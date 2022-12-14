# Generated by Django 4.1.3 on 2022-11-30 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_profesor_alter_orderedalum_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Examen_Final',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hora_fecha', models.DateTimeField()),
                ('curso', models.CharField(max_length=30)),
                ('evaluador', models.CharField(max_length=30)),
                ('duracion_examen', models.IntegerField()),
                ('numero_preguntas', models.IntegerField()),
                ('puntaje_total', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Examen_Final',
                'verbose_name_plural': 'Examenes_Finales',
            },
        ),
    ]
