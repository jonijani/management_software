# Generated by Django 3.2.13 on 2022-05-21 20:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Jobs', '0044_auto_20220314_1900'),
        ('Inventories', '0021_remove_ordered_parts_job'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordered_parts',
            name='make',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ordered_make', to='Jobs.make'),
        ),
    ]
