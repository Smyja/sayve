# Generated by Django 3.1.4 on 2021-04-09 15:37

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('escrow', '0013_auto_20210409_1255'),
    ]

    operations = [
        migrations.AddField(
            model_name='sendcoin',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='sendcoin',
            name='amount',
            field=models.DecimalField(decimal_places=2, max_digits=15),
        ),
    ]
