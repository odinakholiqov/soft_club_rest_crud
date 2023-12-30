# Generated by Django 4.1 on 2023-12-19 14:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("gps", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Tracker",
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
                ("version", models.CharField(max_length=10)),
            ],
        ),
        migrations.AddField(
            model_name="vehicle",
            name="tracker",
            field=models.ForeignKey(
                null=True, on_delete=django.db.models.deletion.CASCADE, to="gps.tracker"
            ),
        ),
    ]