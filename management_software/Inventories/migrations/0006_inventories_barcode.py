# Generated by Django 3.2.4 on 2022-03-12 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inventories', '0005_auto_20220307_1649'),
    ]

    operations = [
        migrations.AddField(
            model_name='inventories',
            name='barcode',
            field=models.ImageField(blank=True, upload_to='barcodes/'),
        ),
    ]
