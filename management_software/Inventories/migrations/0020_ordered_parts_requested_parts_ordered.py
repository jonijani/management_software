# Generated by Django 3.2.13 on 2022-05-21 19:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Inventories', '0019_auto_20220521_1912'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordered_parts',
            name='requested_parts_ordered',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='requested_parts_ordered', to='Inventories.request_parts'),
        ),
    ]
