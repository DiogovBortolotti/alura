# Generated by Django 5.0.1 on 2024-01-18 23:09

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo_receitas', '0009_alter_receita_data'),
        ('pessoas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='receita',
            name='pessoa',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='pessoas.pessoa'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='receita',
            name='data',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 1, 18, 20, 9, 16, 997163), null=True),
        ),
    ]
