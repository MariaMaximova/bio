# Generated by Django 3.0.2 on 2020-01-29 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20200125_0812'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_locked',
            field=models.BooleanField(default=False),
        ),
    ]
