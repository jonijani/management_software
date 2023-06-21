# Generated by Django 3.2.13 on 2022-05-10 21:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Jobs', '0044_auto_20220314_1900'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Inventories', '0014_auto_20220510_1913'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ordered_parts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('buying_cost', models.IntegerField()),
                ('part_description', models.CharField(blank=True, max_length=20000, null=True)),
                ('created_date', models.DateTimeField(blank=True, null=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('devices', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ordered_device', to='Jobs.devices')),
                ('job', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='job_ordered_part', to='Jobs.jobs')),
                ('make', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ordered_make', to='Jobs.make')),
                ('model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ordered_model', to='Jobs.model')),
                ('part_colour', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ordered_Part_colour', to='Inventories.part_colour')),
                ('part_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ordered_part_name', to='Inventories.part_name')),
                ('part_status', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ordered_part_status', to='Inventories.part_status')),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ordered_supplier', to='Inventories.supplier')),
            ],
        ),
    ]
