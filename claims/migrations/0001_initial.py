# Generated by Django 5.1.2 on 2024-12-02 09:18

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('vehicle', '__first__'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Claim',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('claim_date', models.DateField(auto_now_add=True)),
                ('accident_date', models.DateField(help_text='Date of the accident.')),
                ('accident_location', models.CharField(help_text='Where the accident occurred.', max_length=200)),
                ('description', models.TextField(help_text='Detailed description of the accident and claim.')),
                ('estimated_damage_cost', models.DecimalField(decimal_places=2, help_text='Estimated cost of damages.', max_digits=10)),
                ('police_report_number', models.CharField(blank=True, help_text='Police report reference, if applicable.', max_length=50, null=True)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Rejected', 'Rejected'), ('Closed', 'Closed')], default='Pending', max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('claim_officer', models.ForeignKey(blank=True, help_text='The officer assigned to this claim.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='handled_claims', to=settings.AUTH_USER_MODEL)),
                ('claimant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='claims', to=settings.AUTH_USER_MODEL)),
                ('vehicle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='claims', to='vehicle.vehicle')),
            ],
        ),
    ]
