# Generated by Django 2.1.15 on 2023-11-08 22:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reto', '0003_villano'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pelea',
            fields=[
                ('id_pelea', models.AutoField(primary_key=True, serialize=False)),
                ('resultado', models.CharField(max_length=100)),
                ('id_heroe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reto.Heroe')),
                ('id_villano', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reto.Villano')),
            ],
        ),
    ]
