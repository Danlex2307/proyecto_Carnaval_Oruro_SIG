# Generated by Django 4.2.6 on 2024-06-24 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0008_calificacion"),
    ]

    operations = [
        migrations.AddField(
            model_name="comentario",
            name="rating",
            field=models.IntegerField(blank=True, null=True),
        ),
    ]