# Generated by Django 3.1.4 on 2021-04-05 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('escrow', '0006_auto_20210405_1953'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(max_length=64, null=True),
        ),
    ]
