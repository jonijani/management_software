# Generated by Django 3.2.13 on 2022-07-24 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Retail', '0015_daily_totals'),
    ]

    operations = [
        migrations.AlterField(
            model_name='daily_totals',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
