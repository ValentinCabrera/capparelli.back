# Generated by Django 4.2.7 on 2023-11-22 15:23

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("user", "0002_user_date_joined_user_groups_user_is_active_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="client",
            name="user_ptr",
        ),
        migrations.DeleteModel(
            name="Admin",
        ),
        migrations.DeleteModel(
            name="Client",
        ),
    ]