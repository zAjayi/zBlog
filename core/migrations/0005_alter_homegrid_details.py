# Generated by Django 4.2.2 on 2023-08-06 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homegrid',
            name='details',
            field=models.CharField(default='some strin', max_length=5000),
        ),
    ]