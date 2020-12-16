# Generated by Django 3.0.5 on 2020-12-16 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_media', '0006_auto_20201216_0930'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='title',
            name='genre',
        ),
        migrations.AddField(
            model_name='title',
            name='genre',
            field=models.ManyToManyField(blank=True, to='api_media.Genre'),
        ),
    ]
