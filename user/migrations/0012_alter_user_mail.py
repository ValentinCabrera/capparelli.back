# Generated by Django 4.2.7 on 2023-11-20 02:17

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("user", "0011_admin"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="mail",
            field=models.CharField(max_length=50, unique=True),
        ),
    ]