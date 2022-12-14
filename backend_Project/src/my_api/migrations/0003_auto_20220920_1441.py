# Generated by Django 3.1 on 2022-09-20 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_api', '0002_acount'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='acount',
            name='acount_id',
        ),
        migrations.AddField(
            model_name='acount',
            name='acount_name',
            field=models.CharField(blank=True, max_length=255, verbose_name='アカウント名'),
        ),
        migrations.AlterField(
            model_name='acount',
            name='password',
            field=models.UUIDField(blank=True, verbose_name='パスワード'),
        ),
    ]
