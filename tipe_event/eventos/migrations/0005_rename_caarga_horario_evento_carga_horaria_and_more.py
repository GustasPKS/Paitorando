# Generated by Django 4.2 on 2023-04-26 00:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0004_rename_caarga_horaria_evento_caarga_horario'),
    ]

    operations = [
        migrations.RenameField(
            model_name='evento',
            old_name='caarga_horario',
            new_name='carga_horaria',
        ),
        migrations.RenameField(
            model_name='evento',
            old_name='data_inico',
            new_name='data_inicio',
        ),
    ]
