# Generated by Django 5.1.2 on 2024-12-14 11:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_insuredcustomer'),
        ('claims', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='claim',
            name='claimant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='claims', to='accounts.insuredcustomer'),
        ),
    ]
