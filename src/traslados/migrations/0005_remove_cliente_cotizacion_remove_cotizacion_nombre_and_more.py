# Generated by Django 5.1.4 on 2024-12-31 04:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('traslados', '0004_remove_cotizacion_precio_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='cotizacion',
        ),
        migrations.RemoveField(
            model_name='cotizacion',
            name='nombre',
        ),
        migrations.AddField(
            model_name='cliente',
            name='paquete',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='traslados.paquete'),
        ),
        migrations.AddField(
            model_name='cotizacion',
            name='cliente',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='traslados.cliente'),
        ),
        migrations.AlterField(
            model_name='paquete',
            name='categoria',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='traslados.categoria'),
        ),
    ]