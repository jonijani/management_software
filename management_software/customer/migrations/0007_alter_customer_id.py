# Generated by Django 3.2.4 on 2022-01-29 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0006_rename_date_time_customer_created_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]