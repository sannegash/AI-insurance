# Generated by Django 4.2.18 on 2025-02-05 12:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle', '0003_vehicle_customer'),
        ('policies', '0007_alter_policy_vehicle'),
    ]

    operations = [
        migrations.AlterField(
            model_name='policy',
            name='vehicle',
            field=models.OneToOneField(help_text='Vehicle covered by this policy.', on_delete=django.db.models.deletion.CASCADE, related_name='policy', to='vehicle.vehicle', to_field='chassis_number'),
        ),
    ]
