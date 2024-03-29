# Generated by Django 5.0.2 on 2024-02-20 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ListaAtividades',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('descricao', models.TextField(blank=True, null=True)),
                ('data_agendada', models.DateField()),
                ('data_registro_agenda', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'Lista_tarefas',
            },
        ),
    ]
