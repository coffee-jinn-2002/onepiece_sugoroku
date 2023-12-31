# Generated by Django 4.2.6 on 2023-10-20 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="GameState",
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
                ("player_position", models.IntegerField(default=1)),
                ("cpu_position", models.IntegerField(default=1)),
                ("is_player_turn", models.BooleanField(default=True)),
                ("is_game_over", models.BooleanField(default=False)),
                ("dice", models.IntegerField(default=0)),
            ],
        ),
    ]
