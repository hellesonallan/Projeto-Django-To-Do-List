# Generated by Django 5.0.6 on 2024-07-02 23:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Tarefas",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("titulo", models.CharField(max_length=50)),
                ("data_inicio", models.DateTimeField(auto_now_add=True)),
                ("data_final", models.DateTimeField()),
                ("data_terminada", models.DateTimeField()),
            ],
        ),
    ]
