# Generated by Django 5.1.2 on 2024-12-12 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("library", "0003_alter_book_options"),
    ]

    operations = [
        migrations.AddField(
            model_name="book",
            name="recommend",
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="book",
            name="review",
            field=models.TextField(blank=True, null=True),
        ),
    ]
