# Generated by Django 3.0.2 on 2020-01-29 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0007_testsuite_correct_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testsuite',
            name='correct_count',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]
