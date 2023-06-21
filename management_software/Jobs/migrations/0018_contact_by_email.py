# Generated by Django 3.2.4 on 2022-02-15 19:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Jobs', '0017_reciepts'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact_by_email',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Jobs.jobs')),
            ],
        ),
    ]
