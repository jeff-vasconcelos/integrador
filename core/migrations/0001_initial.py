# Generated by Django 2.2.23 on 2021-11-01 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Configuracao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(blank=True, max_length=84, null=True)),
                ('password', models.CharField(blank=True, max_length=128, null=True)),
                ('empresa', models.CharField(blank=True, max_length=84, null=True)),
                ('empresa_id', models.CharField(blank=True, max_length=84, null=True)),
                ('user_db', models.CharField(blank=True, max_length=84, null=True)),
                ('password_db', models.CharField(blank=True, max_length=84, null=True)),
                ('host_db', models.CharField(blank=True, max_length=84, null=True)),
                ('port_db', models.CharField(blank=True, max_length=84, null=True)),
                ('service_db', models.CharField(blank=True, max_length=84, null=True)),
            ],
            options={
                'verbose_name': 'Configuração',
                'verbose_name_plural': 'Configurações',
            },
        ),
        migrations.CreateModel(
            name='Registro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'verbose_name': 'Registro',
                'verbose_name_plural': 'Registros',
            },
        ),
    ]