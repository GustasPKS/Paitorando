# Generated by Django 4.2 on 2023-04-26 01:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0005_rename_caarga_horario_evento_carga_horaria_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='evento',
            old_name='carga_horaria',
            new_name='caarga_horaria',
        ),
        migrations.RenameField(
            model_name='evento',
            old_name='data_inicio',
            new_name='data_inico',
        ),
    ]
