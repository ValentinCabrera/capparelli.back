# Generated by Django 4.2.7 on 2023-11-29 03:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("order", "0002_alter_orderstatechange_order"),
    ]

    operations = [
        migrations.CreateModel(
            name="Discount",
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
                ("code", models.CharField(max_length=15)),
                ("percentage", models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name="OrderDiscount",
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
                (
                    "discount",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.RESTRICT,
                        to="order.discount",
                    ),
                ),
                (
                    "order",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.RESTRICT,
                        related_name="discounts",
                        to="order.order",
                    ),
                ),
            ],
        ),
    ]