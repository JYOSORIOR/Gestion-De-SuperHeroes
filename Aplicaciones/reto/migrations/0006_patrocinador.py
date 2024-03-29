# Generated by Django 2.1.15 on 2023-11-10 16:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reto', '0005_auto_20231108_2215'),
    ]

    operations = [
        migrations.CreateModel(
            name='Patrocinador',
            fields=[
                ('id_patrocinador', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('monto', models.PositiveSmallIntegerField(null=True)),
                ('origenDinero', models.CharField(max_length=100)),
                ('id_heroe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reto.Heroe')),
            ],
        ),
    ]
