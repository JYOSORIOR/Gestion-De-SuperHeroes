# Generated by Django 4.2.7 on 2023-11-13 04:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("reto", "0012_auto_20231112_2147"),
    ]

    operations = [
        migrations.RemoveField(model_name="pelea", name="id_villano",),
        migrations.DeleteModel(name="Villano",),
    ]
