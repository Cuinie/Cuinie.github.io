# Generated by Django 4.2.17 on 2025-01-14 06:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='IncidentType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Incident',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('incident_number', models.CharField(max_length=50, unique=True)),
                ('year', models.IntegerField(default=2025)),
                ('date_submitted', models.DateTimeField()),
                ('reporter_name', models.CharField(max_length=100)),
                ('position', models.CharField(max_length=100)),
                ('department', models.CharField(max_length=100)),
                ('status', models.CharField(choices=[('new', 'New'), ('in_progress', 'In Progress'), ('resolved', 'Resolved'), ('closed', 'Closed')], default='new', max_length=20)),
                ('description', models.TextField(default='Not provided', verbose_name='Description of Incident')),
                ('scope', models.TextField(default='Not provided', verbose_name='Scope of Incident')),
                ('systems_affected_count', models.IntegerField(verbose_name='Estimated Quantity of Systems Affected')),
                ('data_subjects_count', models.IntegerField(verbose_name='Estimated Quantity of Data Subjects Affected')),
                ('data_subjects_groups', models.TextField(default='Not provided', verbose_name='Data Subjects Affected')),
                ('additional_scope_info', models.TextField(blank=True, null=True, verbose_name='Additional Scope Information')),
                ('impact_level', models.CharField(choices=[('low', 'Low'), ('medium', 'Medium'), ('high', 'High'), ('critical', 'Critical')], max_length=20, verbose_name='Impact of Incident')),
                ('estimated_cost', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Estimated Total Cost Incurred')),
                ('additional_impact_info', models.TextField(blank=True, null=True, verbose_name='Additional Impact Information')),
                ('data_sensitivity', models.TextField(default='Not provided', verbose_name='Sensitivity of Affected Data/Information')),
                ('data_quantity', models.TextField(default='Not provided', verbose_name='Quantity of Data/Information Affected')),
                ('additional_data_info', models.TextField(blank=True, null=True, verbose_name='Additional Affected Data Information')),
                ('attack_sources', models.TextField(default='Not specified', verbose_name='Attack Sources')),
                ('attack_destinations', models.TextField(default='Not specified', verbose_name='Attack Destinations')),
                ('affected_ips', models.TextField(default='Not specified', verbose_name='IP Addresses of Affected Systems')),
                ('affected_domains', models.TextField(default='Not specified', verbose_name='Domain Names of Affected Systems')),
                ('system_functions', models.TextField(default='Not specified', verbose_name='Primary Functions of Affected Systems')),
                ('operating_systems', models.TextField(default='Not specified', verbose_name='Operating Systems of Affected Systems')),
                ('patch_levels', models.TextField(default='Not specified', verbose_name='Patch Level of Affected Systems')),
                ('security_software', models.TextField(default='Not specified', verbose_name='Security Software Loaded on Affected Systems')),
                ('physical_location', models.TextField(default='Not specified', verbose_name='Physical Location of Affected Systems')),
                ('additional_system_details', models.TextField(blank=True, null=True, verbose_name='Additional System Details')),
                ('affected_user_titles', models.TextField(default='Not specified', verbose_name='Job Titles of Affected Users')),
                ('access_levels', models.TextField(default='Not specified', verbose_name='System Access Levels or Rights of Affected Users')),
                ('additional_user_details', models.TextField(blank=True, null=True, verbose_name='Additional User Details')),
                ('discovery_date', models.DateTimeField(verbose_name='Date and Time of Discovery')),
                ('incident_date', models.DateTimeField(verbose_name='Date and Time When the Actual Incident Occurred')),
                ('containment_date', models.DateTimeField(blank=True, null=True, verbose_name='Date and Time When the Incident Was Contained')),
                ('detailed_timeline', models.TextField(default='Not provided', verbose_name='Detailed Incident Timeline')),
                ('attachments', models.FileField(blank=True, null=True, upload_to='incident_attachments/', verbose_name='Supporting Documents')),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('dpo_remarks', models.TextField(blank=True, null=True, verbose_name='DPO Remarks')),
                ('dpo_attachments', models.FileField(blank=True, null=True, upload_to='dpo_attachments/', verbose_name='DPO Supporting Documents')),
                ('actions_identify_resources', models.TextField(blank=True, null=True, verbose_name='Actions Taken to Identify Affected Resources')),
                ('actions_address_incident', models.TextField(blank=True, null=True, verbose_name='Actions Taken to Address the Incident')),
                ('actions_mitigate_harm', models.TextField(blank=True, null=True, verbose_name='Actions Performed to Mitigate Possible Harm')),
                ('actions_prevent_similar', models.TextField(blank=True, null=True, verbose_name='Actions Taken to Prevent Similar Incidents')),
                ('additional_actions_planned', models.TextField(blank=True, null=True, verbose_name='Details of Additional Actions Planned')),
                ('dpo_additional_info', models.TextField(blank=True, null=True, verbose_name='Additional Information for DPO')),
                ('incident_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.incidenttype')),
            ],
            options={
                'ordering': ['-date_submitted'],
            },
        ),
    ]
