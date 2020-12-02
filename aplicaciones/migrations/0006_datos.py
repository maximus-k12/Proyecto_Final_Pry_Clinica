# Generated by Django 3.1.3 on 2020-11-15 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicaciones', '0005_auto_20201115_1748'),
    ]

    operations = [
        migrations.CreateModel(
            name='Datos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NOMBRE', models.CharField(max_length=50)),
                ('EDAD', models.CharField(max_length=50)),
                ('FECHA_EXAMEN', models.CharField(max_length=50)),
                ('DIRECCION', models.CharField(max_length=50)),
                ('TELEFONO', models.CharField(max_length=50)),
                ('tipo_genero', models.IntegerField(choices=[[0, 'Soltero'], [1, 'Casado']])),
                ('tipo_sexo', models.IntegerField(choices=[[2, 'Hombre'], [3, 'Mujer']])),
                ('Informacion_Adicional', models.TextField()),
            ],
        ),
    ]