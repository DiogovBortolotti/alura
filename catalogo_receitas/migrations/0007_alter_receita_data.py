# Generated by Django 5.0.1 on 2024-01-18 22:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo_receitas', '0006_remove_receita_data_receita_alter_receita_data_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receita',
            name='data',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 1, 18, 19, 52, 9, 446734), null=True),
        ),
    ]