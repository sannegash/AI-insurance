# Generated by Django 5.1.2 on 2024-12-23 05:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_delete_insuredcustomer'),
        ('policies', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='insurancepolicy',
            name='policy_holder',
            field=models.ForeignKey(help_text='The policyholder (user who owns the policy).', on_delete=django.db.models.deletion.CASCADE, related_name='policies', to='accounts.newcustomer'),
        ),
    ]
