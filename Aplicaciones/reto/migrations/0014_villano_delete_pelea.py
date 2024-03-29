# Generated by Django 4.2.7 on 2023-11-13 04:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("reto", "0013_remove_pelea_id_villano_delete_villano"),
    ]

    operations = [
        migrations.CreateModel(
            name="Villano",
            fields=[
                ("id_villano", models.AutoField(primary_key=True, serialize=False)),
                ("nombre", models.CharField(max_length=100)),
                ("edad", models.PositiveSmallIntegerField(null=True)),
                ("origen", models.CharField(max_length=100)),
                ("habilidades", models.TextField(blank=True)),
                ("debilidad", models.TextField(blank=True)),
            ],
        ),
        migrations.DeleteModel(name="Pelea",),
    ]
