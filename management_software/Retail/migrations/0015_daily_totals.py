# Generated by Django 3.2.13 on 2022-07-24 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Retail', '0014_email_admin_list'),
    ]

    operations = [
        migrations.CreateModel(
            name='Daily_totals',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.CharField(blank=True, max_length=250, null=True)),
                ('date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]
