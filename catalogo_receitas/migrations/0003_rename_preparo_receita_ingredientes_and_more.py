# Generated by Django 5.0.1 on 2024-01-10 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo_receitas', '0002_receita_receita_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='receita',
            old_name='preparo',
            new_name='ingredientes',
        ),
        migrations.AddField(
            model_name='receita',
            name='modo_preparo',
            field=models.CharField(default=0, max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='receita',
            name='tempo_preparo',
            field=models.CharField(default=0, max_length=250),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='receita',
            name='rendimento',
            field=models.CharField(max_length=120),
        ),
    ]
