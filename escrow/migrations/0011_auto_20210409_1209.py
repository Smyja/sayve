# Generated by Django 3.1.4 on 2021-04-09 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('escrow', '0010_auto_20210409_1208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sendcoins',
            name='receiver',
            field=models.CharField(default=None, max_length=150),
        ),
    ]