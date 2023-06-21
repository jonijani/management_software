# Generated by Django 3.2.4 on 2022-02-18 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Jobs', '0023_complete_job_completed_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='complete_job',
            name='completed_on',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='complete_job',
            name='cost_com',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='complete_job',
            name='payment_status_com',
            field=models.CharField(blank=True, choices=[('PAID', 'PAID'), ('UNPAID', 'UNPAID'), ('CREDIT NOTE', 'CREDIT NOTE'), ('REFUND', 'REFUND')], max_length=250, null=True),
        ),
    ]