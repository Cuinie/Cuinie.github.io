# Generated by Django 4.2.17 on 2025-01-14 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_incident_attachment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='incident',
            name='dpo_additional_info',
        ),
        migrations.RemoveField(
            model_name='incident',
            name='dpo_attachments',
        ),
        migrations.AddField(
            model_name='incident',
            name='dpo_evaluation_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='incident',
            name='dpo_status',
            field=models.CharField(choices=[('pending', 'Pending Review'), ('approved', 'Approved'), ('needs_action', 'Needs Action'), ('rejected', 'Rejected')], default='pending', max_length=20),
        ),
        migrations.AlterField(
            model_name='incident',
            name='actions_address_incident',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='incident',
            name='actions_identify_resources',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='incident',
            name='actions_mitigate_harm',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='incident',
            name='actions_prevent_similar',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='incident',
            name='additional_actions_planned',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='incident',
            name='dpo_remarks',
            field=models.TextField(blank=True, null=True),
        ),
    ]
