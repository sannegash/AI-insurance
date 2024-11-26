# Generated by Django 5.1.3 on 2024-11-26 12:50

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('vehicle', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='InsurancePolicy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('policy_number', models.CharField(help_text='Unique policy number.', max_length=20, unique=True)),
                ('insured_name', models.CharField(help_text='Name of the insured individual or organization.', max_length=100)),
                ('policy_type', models.CharField(choices=[('Comprehensive', 'Comprehensive'), ('Third-Party', 'Third-Party'), ('Third-Party, Fire and Theft', 'Third-Party, Fire and Theft')], help_text='Type of insurance policy.', max_length=30)),
                ('coverage_start_date', models.DateField(help_text='Start date of the coverage.')),
                ('coverage_end_date', models.DateField(help_text='End date of the coverage.')),
                ('premium_amount', models.DecimalField(decimal_places=2, help_text='The premium amount for the policy.', max_digits=10)),
                ('insured_value', models.DecimalField(decimal_places=2, help_text='The value of the vehicle insured under this policy.', max_digits=10)),
                ('status', models.CharField(choices=[('Active', 'Active'), ('Expired', 'Expired'), ('Cancelled', 'Cancelled')], default='Active', max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('policy_holder', models.ForeignKey(help_text='The policyholder (user who owns the policy).', on_delete=django.db.models.deletion.CASCADE, related_name='policies', to=settings.AUTH_USER_MODEL)),
                ('vehicle', models.ForeignKey(help_text='Vehicle covered by this policy.', on_delete=django.db.models.deletion.CASCADE, related_name='policies', to='vehicle.vehicle')),
            ],
        ),
    ]
