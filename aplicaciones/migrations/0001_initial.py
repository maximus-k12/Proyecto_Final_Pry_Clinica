# Generated by Django 3.1.3 on 2020-11-15 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=50)),
                ('Edad', models.IntegerField()),
                ('Sexo', models.TextField()),
                ('Direcion', models.TextField()),
                ('Telefono', models.TextField()),
                ('Fecha_de_consulta', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Tratamiento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=50)),
                ('Tratamiento', models.TextField()),
                ('Descripcion', models.TextField()),
                ('Fecha_de_cita', models.DateField()),
            ],
        ),
    ]
