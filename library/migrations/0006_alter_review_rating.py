# Generated by Django 5.1.2 on 2024-12-16 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0005_review'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.IntegerField(),
        ),
    ]
