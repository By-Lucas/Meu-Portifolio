# Generated by Django 4.0.1 on 2022-03-08 02:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_pix', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='charge',
            name='status',
            field=models.CharField(default='DESATIVADO', max_length=50),
        ),
    ]
