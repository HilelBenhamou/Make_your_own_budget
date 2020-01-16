# Generated by Django 3.0.2 on 2020-01-12 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_account_date_creation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='balance',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='account',
            name='balance_start',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='amount',
            field=models.FloatField(),
        ),
    ]
