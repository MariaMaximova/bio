# Generated by Django 3.0.2 on 2020-01-29 17:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sessions', '0001_initial'),
        ('questions', '0010_auto_20200129_1740'),
    ]

    operations = [
        migrations.AddField(
            model_name='testanswer',
            name='no',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='testsuite',
            name='session',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='test_suites', to='sessions.Session'),
            preserve_default=False,
        ),
    ]