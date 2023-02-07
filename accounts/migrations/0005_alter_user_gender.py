# Generated by Django 4.1 on 2023-02-07 03:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0004_alter_user_username"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="gender",
            field=models.CharField(
                choices=[("male", "male"), ("female", "female"), ("other", "other")],
                max_length=10,
                null=True,
            ),
        ),
    ]