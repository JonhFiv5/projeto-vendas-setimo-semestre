# Generated by Django 4.0.4 on 2022-05-19 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Venda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('onde_comprou', models.CharField(max_length=20, verbose_name='Onde Comprou')),
                ('genero', models.CharField(max_length=20, verbose_name='Gênero')),
                ('tipo_roupa', models.CharField(max_length=40, verbose_name='Tipo de Roupa')),
                ('cor', models.CharField(max_length=40, verbose_name='Cor')),
                ('tamanho', models.CharField(max_length=10, verbose_name='Tamanho')),
                ('preco', models.FloatField(verbose_name='Preço')),
                ('estacao', models.CharField(max_length=10, verbose_name='Estação')),
                ('mes', models.CharField(max_length=15, verbose_name='Mês')),
            ],
        ),
    ]