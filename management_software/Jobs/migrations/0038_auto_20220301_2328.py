# Generated by Django 3.2.4 on 2022-03-01 23:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Jobs', '0037_auto_20220301_2312'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jobs',
            name='delivered',
        ),
        migrations.AddField(
            model_name='delivered',
            name='delivered',
            field=models.BooleanField(default=False),
        ),
    ]
