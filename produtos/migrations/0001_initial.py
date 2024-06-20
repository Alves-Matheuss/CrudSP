# Generated by Django 5.0.6 on 2024-06-20 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('descricao', models.TextField()),
                ('preco', models.DecimalField(decimal_places=2, max_digits=10)),
                ('unidade_medida', models.CharField(choices=[('kg', 'Kilograma'), ('g', 'Grama'), ('un', 'Unidade')], max_length=3)),
                ('estoque', models.PositiveIntegerField()),
            ],
        ),
    ]
