# Generated by Django 5.1.2 on 2024-10-29 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=150, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=150, verbose_name='Фамилия')),
                ('year', models.CharField(choices=[('first', 'Первый курс'), ('second', 'Второй курс'), ('third', 'Третий курс'), ('fourth', 'Четвертый курс')], default='fourth', max_length=6, verbose_name='Курс')),
            ],
            options={
                'verbose_name': 'студент',
                'verbose_name_plural': 'студенты',
                'ordering': ['last_name'],
            },
        ),
    ]
