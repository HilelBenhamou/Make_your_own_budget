# Generated by Django 3.0.2 on 2020-01-15 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_auto_20200112_1151'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='currency',
            field=models.CharField(default='₪', max_length=30),
        ),
        migrations.AddField(
            model_name='transaction',
            name='currency',
            field=models.CharField(default='₪', max_length=30),
        ),
    ]
