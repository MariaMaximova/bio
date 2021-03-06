# Generated by Django 3.0.2 on 2020-01-25 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0003_auto_20200125_1002'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='attachment',
        ),
        migrations.AddField(
            model_name='answer',
            name='image',
            field=models.ImageField(default='', upload_to='img'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='question',
            name='image',
            field=models.ImageField(default='', upload_to='img'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Picture',
        ),
    ]
