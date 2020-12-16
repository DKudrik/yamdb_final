# Generated by Django 3.0.5 on 2020-12-14 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='yamdbuser',
            options={'verbose_name': 'Пользователь', 'verbose_name_plural': 'Пользователи'},
        ),
        migrations.AlterField(
            model_name='yamdbuser',
            name='role',
            field=models.CharField(blank=True, choices=[('user', 'User'), ('moderator', 'Moderator'), ('admin', 'Admin')], max_length=15, verbose_name='Роль пользователя'),
        ),
    ]