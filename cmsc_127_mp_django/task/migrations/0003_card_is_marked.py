# Generated by Django 3.2.4 on 2021-06-25 02:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='is_marked',
            field=models.BooleanField(default=False),
        ),
    ]
