# Generated by Django 3.2 on 2021-11-06 03:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('idUsuario', models.PositiveSmallIntegerField(primary_key=True, serialize=False)),
                ('cedula', models.CharField(max_length=10)),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('celular', models.CharField(max_length=15)),
                ('email', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Vehiculo',
            fields=[
                ('idVehiculo', models.PositiveSmallIntegerField(primary_key=True, serialize=False)),
                ('placa', models.CharField(max_length=6)),
                ('color', models.CharField(max_length=10)),
                ('marca', models.CharField(max_length=10)),
                ('modelo', models.CharField(max_length=10)),
                ('propietario', models.CharField(max_length=50)),
                ('idUsuario', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='gestion.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Pago',
            fields=[
                ('idPago', models.PositiveSmallIntegerField(primary_key=True, serialize=False)),
                ('fecha', models.DateTimeField(verbose_name='date published')),
                ('idUsuario', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='gestion.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Celda',
            fields=[
                ('idCelda', models.PositiveSmallIntegerField(primary_key=True, serialize=False)),
                ('dimensiones', models.CharField(max_length=50)),
                ('idVehiculo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='gestion.vehiculo')),
            ],
        ),
    ]
