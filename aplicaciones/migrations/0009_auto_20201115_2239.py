# Generated by Django 3.1.3 on 2020-11-15 22:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aplicaciones', '0008_datos_informacion_adicional_sobre_el_paciente'),
    ]

    operations = [
        migrations.RenameField(
            model_name='datos',
            old_name='tipo_genero',
            new_name='estado_civil',
        ),
        migrations.RenameField(
            model_name='datos',
            old_name='tipo_sexo',
            new_name='sexo',
        ),
    ]
