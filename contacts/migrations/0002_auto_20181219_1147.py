# Generated by Django 2.1.4 on 2018-12-19 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacts',
            name='created_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='发送时间'),
        ),
    ]
