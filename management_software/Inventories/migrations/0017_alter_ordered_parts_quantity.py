# Generated by Django 3.2.13 on 2022-05-21 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inventories', '0016_auto_20220510_2201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordered_parts',
            name='quantity',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]