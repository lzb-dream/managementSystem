# Generated by Django 4.2.2 on 2023-08-15 10:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Materiel",
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
                ("cargo_name", models.CharField(default=None, max_length=200)),
                ("cargo_info", models.JSONField(default=list)),
                ("add_time", models.DateTimeField(null=True)),
                ("quantity_in_storage", models.IntegerField(default=0)),
                ("remark", models.CharField(default=None, max_length=200)),
            ],
            options={
                "verbose_name": "货物管理",
                "verbose_name_plural": "货物管理",
                "db_table": "materiel",
            },
        ),
        migrations.CreateModel(
            name="Users",
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
                    "username",
                    models.CharField(default="用户", max_length=255, verbose_name="用户"),
                ),
                (
                    "account_number",
                    models.CharField(max_length=10, unique=True, verbose_name="账号"),
                ),
                ("password", models.CharField(max_length=20, verbose_name="密码")),
                ("addTime", models.DateTimeField(auto_now_add=True)),
                (
                    "status",
                    models.IntegerField(
                        choices=[(0, "禁用"), (1, "管理员"), (2, "超级管理员")], default=0
                    ),
                ),
            ],
            options={
                "verbose_name": "所有用户",
                "verbose_name_plural": "所有用户",
                "db_table": "users",
            },
        ),
        migrations.CreateModel(
            name="UseLogList",
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
                ("user_class", models.CharField(max_length=20)),
                ("user_log", models.CharField(max_length=255)),
                (
                    "submitter",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="babatuoshimingAPI.users",
                    ),
                ),
            ],
            options={
                "verbose_name": "所有用户",
                "verbose_name_plural": "所有用户",
                "db_table": "Use_log_list",
            },
        ),
    ]
