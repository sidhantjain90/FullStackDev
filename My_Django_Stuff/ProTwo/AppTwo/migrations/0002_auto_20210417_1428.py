# Generated by Django 3.2 on 2021-04-17 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppTwo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(max_length=264),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(max_length=264),
        ),
    ]
