# Generated by Django 4.1 on 2023-01-19 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Board",
            fields=[
                ("post_number", models.AutoField(primary_key=True, serialize=False)),
                ("contents", models.CharField(blank=True, max_length=1000, null=True)),
            ],
            options={"db_table": "board", "managed": False,},
        ),
        migrations.CreateModel(
            name="Users",
            fields=[
                ("member_number", models.AutoField(primary_key=True, serialize=False)),
                ("id", models.CharField(max_length=100, unique=True)),
                ("password", models.CharField(max_length=100)),
                ("name", models.CharField(max_length=100)),
                ("age", models.IntegerField(blank=True, null=True)),
                ("gender", models.CharField(blank=True, max_length=10, null=True)),
                ("email", models.CharField(blank=True, max_length=50, null=True)),
                ("registration_date", models.DateField(blank=True, null=True)),
                ("latest_login", models.DateField(blank=True, null=True)),
            ],
            options={"db_table": "users", "managed": False,},
        ),
    ]
