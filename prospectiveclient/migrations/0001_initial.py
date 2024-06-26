# Generated by Django 4.2.11 on 2024-05-07 21:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('team', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ProspectiveClient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Имя')),
                ('email', models.EmailField(max_length=254, verbose_name='Почта')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('status', models.CharField(choices=[('Новый клиент', 'Новый клиент'), ('Уже связались', 'Уже связались'), ('В работе', 'В работе'), ('Упущен', 'Упущен')], default='Новый клиент', max_length=45, verbose_name='Статус')),
                ('priority', models.CharField(choices=[('Низкий приоритет', 'Низкий приоритет'), ('Средний приоритет', 'Средний приоритет'), ('Высокий приоритет', 'Высокий приоритет')], default='Средний приоритет', max_length=45, verbose_name='Приоритет')),
                ('converted_to_client', models.BooleanField(default=False, verbose_name='Стал клиентом')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Создано в')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='Изменено в')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='clients', to=settings.AUTH_USER_MODEL, verbose_name='Создано кем')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='prospectiveclients', to='team.team', verbose_name='Состоит в команде')),
            ],
            options={
                'verbose_name': 'Потенциальный клиент',
                'verbose_name_plural': 'Потенциальные клиенты',
                'db_table': 'prospective_client',
            },
        ),
    ]
