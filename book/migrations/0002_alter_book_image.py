# Generated by Django 5.1.1 on 2024-09-29 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("book", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="book",
            name="image",
            field=models.ImageField(upload_to="book/images/", verbose_name="书籍海报"),
        ),
    ]
