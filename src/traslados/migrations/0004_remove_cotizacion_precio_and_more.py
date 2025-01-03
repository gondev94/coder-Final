# Generated by Django 5.1.4 on 2024-12-31 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('traslados', '0003_cotizacion_cliente_flete_paquete_cotizacion_paquete_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cotizacion',
            name='precio',
        ),
        migrations.RemoveField(
            model_name='paquete',
            name='precio_por_km',
        ),
        migrations.RemoveField(
            model_name='paquete',
            name='total',
        ),
        migrations.RemoveField(
            model_name='transportista',
            name='cotizacion',
        ),
        migrations.AddField(
            model_name='cotizacion',
            name='precio_por_km',
            field=models.IntegerField(default=1400),
        ),
        migrations.AddField(
            model_name='cotizacion',
            name='total',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
    ]
