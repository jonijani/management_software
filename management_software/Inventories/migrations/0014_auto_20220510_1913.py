# Generated by Django 3.2.13 on 2022-05-10 19:13

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Jobs', '0044_auto_20220314_1900'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Inventories', '0013_inventories_description'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Order_parts',
            new_name='Request_parts',
        ),
        migrations.RemoveField(
            model_name='inventories',
            name='description',
        ),
    ]
