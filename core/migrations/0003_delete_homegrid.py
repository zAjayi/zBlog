# Generated by Django 4.2.2 on 2023-08-06 20:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_homegrid_details_alter_homegrid_title'),
    ]

    operations = [
        migrations.DeleteModel(
            name='HomeGrid',
        ),
    ]
