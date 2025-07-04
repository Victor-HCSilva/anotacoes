# Generated by Django 5.2.1 on 2025-06-21 13:46

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Colors',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('cor_de_destaque', models.CharField(choices=[('blue', 'Azul'), ('green', 'Verde'), ('red', 'Vermelho'), ('black', 'Preto'), ('#FFFFFF', 'Branco'), ('#FFC107', 'Amarelo'), ('orange', 'Laranja'), ('#6f42c1', 'Roxo'), ('#d63384', 'Rosa'), ('#0dcaf0', 'Ciano/Turquesa'), ('#6c757d', 'Cinza'), ('#795548', 'Marrom'), ('#FFD700', 'Dourado'), ('#C0C0C0', 'Prata')], default='blue', max_length=19, verbose_name='Cor de destaque')),
                ('cor_do_dia', models.CharField(choices=[('blue', 'Azul'), ('green', 'Verde'), ('red', 'Vermelho'), ('black', 'Preto'), ('#FFFFFF', 'Branco'), ('#FFC107', 'Amarelo'), ('orange', 'Laranja'), ('#6f42c1', 'Roxo'), ('#d63384', 'Rosa'), ('#0dcaf0', 'Ciano/Turquesa'), ('#6c757d', 'Cinza'), ('#795548', 'Marrom'), ('#FFD700', 'Dourado'), ('#C0C0C0', 'Prata')], default='blue', max_length=19, verbose_name='Cor de destaque')),
            ],
        ),
        migrations.CreateModel(
            name='AgendaModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(default='Sem titulo', max_length=200, verbose_name='Título')),
                ('descricao', models.TextField(blank=True, default='Sem descrição', verbose_name='Descrição')),
                ('tipo_de_evento', models.CharField(choices=[('Prova', 'Prova'), ('Atividade', 'Atividade'), ('Terefa', 'Tarefa'), ('Importante', 'Importante'), ('Lembrete', 'Lembrete'), ('Outro', 'Outro')], default=('Lembrete', 'Lembrete'), max_length=20, verbose_name='Tipo de Evento')),
                ('importancia', models.CharField(choices=[('1', 'Mínima'), ('2', 'Mediana'), ('3', 'Máxima')], default=('1', 'Mínima'), max_length=2, verbose_name='Importância')),
                ('dia_do_evento', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Data do evento')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Data de Criação')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Data de Atualização')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuário')),
            ],
            options={
                'ordering': ['dia_do_evento'],
            },
        ),
    ]
