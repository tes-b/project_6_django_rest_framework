# Generated by Django 4.1 on 2023-01-19 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("bbs", "0003_delete_testtable"),
    ]

    operations = [
        migrations.CreateModel(
            name="AuthGroup",
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
                ("name", models.CharField(max_length=150, unique=True)),
            ],
            options={"db_table": "auth_group", "managed": False,},
        ),
        migrations.CreateModel(
            name="AuthGroupPermissions",
            fields=[("id", models.BigAutoField(primary_key=True, serialize=False)),],
            options={"db_table": "auth_group_permissions", "managed": False,},
        ),
        migrations.CreateModel(
            name="AuthPermission",
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
                ("name", models.CharField(max_length=255)),
                ("codename", models.CharField(max_length=100)),
            ],
            options={"db_table": "auth_permission", "managed": False,},
        ),
        migrations.CreateModel(
            name="AuthUser",
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
                ("password", models.CharField(max_length=128)),
                ("last_login", models.DateTimeField(blank=True, null=True)),
                ("is_superuser", models.IntegerField()),
                ("username", models.CharField(max_length=150, unique=True)),
                ("first_name", models.CharField(max_length=150)),
                ("last_name", models.CharField(max_length=150)),
                ("email", models.CharField(max_length=254)),
                ("is_staff", models.IntegerField()),
                ("is_active", models.IntegerField()),
                ("date_joined", models.DateTimeField()),
            ],
            options={"db_table": "auth_user", "managed": False,},
        ),
        migrations.CreateModel(
            name="AuthUserGroups",
            fields=[("id", models.BigAutoField(primary_key=True, serialize=False)),],
            options={"db_table": "auth_user_groups", "managed": False,},
        ),
        migrations.CreateModel(
            name="AuthUserUserPermissions",
            fields=[("id", models.BigAutoField(primary_key=True, serialize=False)),],
            options={"db_table": "auth_user_user_permissions", "managed": False,},
        ),
        migrations.CreateModel(
            name="DjangoAdminLog",
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
                ("action_time", models.DateTimeField()),
                ("object_id", models.TextField(blank=True, null=True)),
                ("object_repr", models.CharField(max_length=200)),
                ("action_flag", models.PositiveSmallIntegerField()),
                ("change_message", models.TextField()),
            ],
            options={"db_table": "django_admin_log", "managed": False,},
        ),
        migrations.CreateModel(
            name="DjangoContentType",
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
                ("app_label", models.CharField(max_length=100)),
                ("model", models.CharField(max_length=100)),
            ],
            options={"db_table": "django_content_type", "managed": False,},
        ),
        migrations.CreateModel(
            name="DjangoMigrations",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                ("app", models.CharField(max_length=255)),
                ("name", models.CharField(max_length=255)),
                ("applied", models.DateTimeField()),
            ],
            options={"db_table": "django_migrations", "managed": False,},
        ),
        migrations.CreateModel(
            name="DjangoSession",
            fields=[
                (
                    "session_key",
                    models.CharField(max_length=40, primary_key=True, serialize=False),
                ),
                ("session_data", models.TextField()),
                ("expire_date", models.DateTimeField()),
            ],
            options={"db_table": "django_session", "managed": False,},
        ),
        migrations.CreateModel(
            name="Test",
            fields=[
                ("post_number", models.AutoField(primary_key=True, serialize=False)),
                ("contents", models.CharField(blank=True, max_length=1000, null=True)),
                ("id", models.IntegerField(blank=True, null=True)),
            ],
            options={"db_table": "test", "managed": False,},
        ),
        migrations.DeleteModel(name="Board",),
        migrations.DeleteModel(name="Users",),
    ]
