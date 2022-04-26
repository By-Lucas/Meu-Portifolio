# Generated by Django 3.2.13 on 2022-04-26 16:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('produtos', '0014_auto_20220426_1331'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='meuspedidos',
            name='produto_id',
        ),
        migrations.AddField(
            model_name='meuspedidos',
            name='produto',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='produtos.produto'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='meuspedidos',
            name='nr_pedido',
            field=models.UUIDField(auto_created=True, default='3137d9b20ea54669bc995b2f689ea1b6', editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='meuspedidos',
            name='quantidade',
            field=models.IntegerField(blank=True, default=1, null=True),
        ),
        migrations.AlterField(
            model_name='meuspedidos',
            name='usuario',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='users.usuario_perfil'),
            preserve_default=False,
        ),
    ]
