# Generated by Django 4.1.2 on 2022-12-08 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fornecedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=40)),
                ('endereco', models.CharField(max_length=50)),
                ('telefone', models.CharField(max_length=11)),
                ('cnpj', models.CharField(max_length=20)),
            ],
        ),
    ]
