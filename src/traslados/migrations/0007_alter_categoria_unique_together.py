# Generated by Django 5.1.4 on 2025-01-01 19:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('traslados', '0006_remove_flete_cotizacion_remove_flete_descripcion_and_more'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='categoria',
            unique_together={('nombre', 'descripcion')},
        ),
    ]