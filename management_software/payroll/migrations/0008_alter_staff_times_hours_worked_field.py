# Generated by Django 3.2.13 on 2022-07-16 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payroll', '0007_alter_staff_times_hours_worked_field'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff_times',
            name='hours_worked_field',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
