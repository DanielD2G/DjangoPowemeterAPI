# Generated by Django 4.1.5 on 2023-01-20 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meter_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meter',
            name='code',
            field=models.CharField(max_length=16, unique=True),
        ),
    ]