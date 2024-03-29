# Generated by Django 3.2.13 on 2022-04-27 17:27

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0040_produto_produto_favorito'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='produto_caregoria',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('imovel', 'Imoveis'), ('eletronicos', 'Eletrônicos'), ('veiculos', 'Veículos'), ('financeiro', 'Financeiro'), ('roupas', 'Roupas'), ('celulares', 'Celulares'), ('moveis', 'Moveis'), ('eletro_domesticos', 'Eletro Doméstico'), ('dinheiro', 'Dinheiro'), ('outros', 'Outros')], max_length=30, null=True),
        ),
    ]
